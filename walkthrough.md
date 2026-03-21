# ESE5880C Project 2 — 出水数据分析完成报告

## 完成情况

所有任务已完成。输出位于 `/home/amoris/5880C/output/`。

---

## 目录结构（调整后）

```
/home/amoris/5880C/
├── biowin/                         # 不变（BioWin 数据）
├── output/                         # ✅ 新建 — 我的成果目录
│   ├── analysis.py                 # 主分析脚本
│   ├── convert_xlsx.py             # xlsx→CSV 转换工具
│   ├── summary.md                  # 文字总结报告
│   ├── cache/                      # CSV 缓存（由 convert_xlsx.py 生成）
│   └── figures/                    # 8 张 PNG 图（300 DPI）
│       ├── fig1_influent_timeseries_cv.png
│       ├── fig2_influent_histogram_cv.png
│       ├── fig3_effluent_timeseries_r.png
│       ├── fig4_effluent_histogram_r.png
│       ├── fig5_exceedance_cdf_r.png
│       ├── fig6_acf_r.png
│       ├── fig7_boxplot_r.png
│       └── fig8_violation_rate_r.png
├── ESE5880C Project 2.pdf
├── 任务.txt / 分工.txt / 要求总结.txt
└── 进水数据.xlsx
```

---

## 数据加载技术

原始 xlsx 文件为 4 MB 压缩、20 MB+ 展开 XML — Python 各种解析器均需≥10分钟。  
**解决方案：** 编写 `convert_xlsx.py`，使用 `ET.iterparse` 流式解析 + 直接写 CSV，  
每个文件转换仅需 **~0.8秒**，共 12 个文件全部转换完成。

---

## 核心统计结果（典型 CV，出水 COD）

| r | 均值 (mg/L) | 标准差 | 超标率 (>60 mg/L) |
|---|-------------|--------|-------------------|
| 0   | 37.59 | 2.93  | **0.00%** |
| 0.3 | 38.24 | 5.87  | **0.74%** |
| 0.6 | 39.18 | 8.17  | **1.96%** |
| 0.9 | 37.92 | 7.48  | **2.29%** |

> 均值几乎不变，但标准差随 r 增大显著增加（+155%），尾部超标风险上升。

---

## 图表预览

### Fig 3 — 出水时间序列（4 种自相关程度）

![Fig 3 Effluent Time Series](/home/amoris/.gemini/antigravity/brain/30910737-8003-495c-9adb-e4ab6f1853ff/fig3.png)

高自相关 (r=0.9) 时，出水 COD 出现显著尖峰，多次突破 60 mg/L 排放标准。

---

### Fig 5 — 超标概率 CCDF

![Fig 5 Exceedance CCDF](/home/amoris/.gemini/antigravity/brain/30910737-8003-495c-9adb-e4ab6f1853ff/fig5.png)

r=0 时出水 COD 分布窄，几乎不超标；r=0.6/0.9 时分布明显右移，超标概率升高。

---

### Fig 6 — ACF 自相关函数

![Fig 6 ACF](/home/amoris/.gemini/antigravity/brain/30910737-8003-495c-9adb-e4ab6f1853ff/fig6.png)

r=0.9 组出水 COD/TSS 的 ACF 在 72 小时 lag 处仍维持 ~0.8，说明系统"记忆"持续时间与进水相关性正比。

---

### Fig 7 — 箱图（均值与标准差）

![Fig 7 Box Plot](/home/amoris/.gemini/antigravity/brain/30910737-8003-495c-9adb-e4ab6f1853ff/fig7.png)

箱体宽度随 r 增大——r=0 时出水 COD IQR 约 6 mg/L，r=0.6 增加至约 11 mg/L，异常值频率和幅度均上升。

---

## 运行方式

```bash
cd /home/amoris/5880C

# Step 1: 转换 xlsx → CSV（已完成，可跳过）
python3 output/convert_xlsx.py

# Step 2: 运行分析，生成所有图和 summary
python3 output/analysis.py
```

依赖：`numpy`, `matplotlib`, `scipy`（均已安装）

---

## 关键结论

1. **自相关使输出更不稳定**：均值基本不变，但 SD 随 r 增大显著增加
2. **超标风险随 r 单调上升**：r=0.9 时 COD 超标率约为 r=0 的 ∞（0% → 2.3%）
3. **TSS 超标极低**：出水 TSS 全程 < 5 mg/L，远低于 30 mg/L 标准（符合 BioWin 系统特性）
4. **ACF 持续性反映系统无法快速消解持续负荷**
