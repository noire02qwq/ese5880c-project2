"""
Fast xlsx → CSV converter for BioWin output files.
Uses streaming iterparse to avoid loading the entire XML into memory.
Writes CSV rows one at a time. Should be significantly faster than 
holding all data in Python lists.

Usage: python3 convert_xlsx.py
"""

import os, re, zipfile, sys, time
import xml.etree.ElementTree as ET

BASE      = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF_DIR  = os.path.join(BASE, "data", "biowin", "biowin data self-related")
NOSELF    = os.path.join(BASE, "data", "biowin", "biowin data NO self-related", "no self-related.xlsx")
CACHE_DIR = os.path.join(BASE, "output", "cache")
os.makedirs(CACHE_DIR, exist_ok=True)

NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'

# Files to convert: (xlsx_path, sheet_index, output_csv_name)
FILES = [
    (NOSELF, 0, "noself_typical_r0.csv"),
    (NOSELF, 1, "noself_small_r0.csv"),
    (NOSELF, 2, "noself_large_r0.csv"),
]
for r in ['0.3', '0.6', '0.9']:
    for cv in ['typical', 'small', 'large']:
        fname = f"{cv} {r} 3yrs.xlsx"
        fpath = os.path.join(SELF_DIR, fname)
        if os.path.exists(fpath):
            safe_r = r.replace('.', '_')
            FILES.append((fpath, 0, f"self_{cv}_r{safe_r}.csv"))


def read_shared_strings(z):
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        data = z.read('xl/sharedStrings.xml')
        root = ET.fromstring(data)
        for si in root.findall(f'{{{NS}}}si'):
            texts = [t.text or '' for t in si.findall(f'.//{{{NS}}}t')]
            shared.append(''.join(texts))
    return shared


def get_sheet_file(z, sheet_index):
    sheet_xmls = sorted(
        [n for n in z.namelist() if re.match(r'xl/worksheets/sheet\d+\.xml', n)],
        key=lambda x: int(re.search(r'sheet(\d+)', x).group(1))
    )
    if sheet_index >= len(sheet_xmls):
        sheet_index = 0
    return sheet_xmls[sheet_index]


def xlsx_to_csv(xlsx_path, sheet_index, csv_path):
    t0 = time.time()
    print(f"  Converting {os.path.basename(xlsx_path)} sheet{sheet_index} → {os.path.basename(csv_path)}")

    with zipfile.ZipFile(xlsx_path, 'r') as z:
        shared = read_shared_strings(z)
        target = get_sheet_file(z, sheet_index)

        with open(csv_path, 'w', encoding='utf-8') as out_f:
            header = None         # list of column names in order
            col_to_idx = {}       # col_letter → position in header
            current_row_num = 0
            current_row_data = {} # col_letter → value string
            current_col = None
            current_type = None
            current_val = None

            with z.open(target) as fh:
                for event, elem in ET.iterparse(fh, events=('start', 'end')):
                    tag = elem.tag.split('}', 1)[-1] if '}' in elem.tag else elem.tag

                    if event == 'start' and tag == 'row':
                        current_row_num = int(elem.get('r', '0'))
                        current_row_data = {}

                    elif event == 'start' and tag == 'c':
                        ref = elem.get('r', '')
                        current_col = ''.join(ch for ch in ref if ch.isalpha())
                        current_type = elem.get('t', '')
                        current_val = None

                    elif event == 'end' and tag == 'v':
                        current_val = elem.text

                    elif event == 'end' and tag == 'c':
                        if current_val is not None and current_col is not None:
                            if current_type == 's':
                                idx = int(current_val)
                                val = shared[idx] if idx < len(shared) else ''
                            else:
                                val = current_val
                            current_row_data[current_col] = val
                        current_col = None
                        current_type = None
                        current_val = None

                    elif event == 'end' and tag == 'row':
                        if current_row_num == 1:
                            # Build header
                            header = []
                            for cl in sorted(current_row_data.keys(),
                                             key=lambda x: (len(x), x)):
                                header.append(current_row_data[cl])
                                col_to_idx[cl] = len(header) - 1
                            out_f.write(','.join(
                                f'"{h}"' for h in header) + '\n')
                        else:
                            if header and current_row_data:
                                row_vals = [''] * len(header)
                                for cl, v in current_row_data.items():
                                    if cl in col_to_idx:
                                        row_vals[col_to_idx[cl]] = v
                                out_f.write(','.join(row_vals) + '\n')
                        elem.clear()

    elapsed = time.time() - t0
    size_kb = os.path.getsize(csv_path) // 1024
    print(f"  Done in {elapsed:.1f}s → {size_kb} KB")


def main():
    print(f"\n=== xlsx → CSV conversion ===")
    for xlsx_path, sheet_idx, csv_name in FILES:
        csv_path = os.path.join(CACHE_DIR, csv_name)
        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 1000:
            print(f"  [skip]  {csv_name} (already converted)")
            continue
        if not os.path.exists(xlsx_path):
            print(f"  [miss]  {os.path.basename(xlsx_path)} (file not found)")
            continue
        try:
            xlsx_to_csv(xlsx_path, sheet_idx, csv_path)
        except Exception as e:
            print(f"  [err]   {csv_name}: {e}")
    print("=== Conversion done ===\n")


if __name__ == '__main__':
    main()
