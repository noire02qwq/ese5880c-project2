# ESE5880C Project 2 — Effluent Data Analysis

废水处理出水数据分析项目 — 研究进水自相关对出水水质的影响。

## 目录结构

```
/home/amoris/ese5880c-project2/
├── data/
│   └── biowin/                    # BioWin 模拟数据
│       ├── biowin data self-related/      # 有自相关的数据 (r=0.3/0.6/0.9)
│       └── biowin data NO self-related/   # 无自相关的数据 (r=0)
├── scripts/
│   ├── analysis.py                # 主分析脚本
│   └── convert_xlsx.py            # xlsx → CSV 转换工具
├── output/
│   ├── figures/                   # 生成的图表 (18张PNG)
│   ├── cache/                     # CSV 缓存数据
│   ├── summary.md                 # 分析报告
│   ├── aor_table.md               # 需氧量汇总表
│   └── parameter_validation.md  # 参数验证报告
└── README.md                      # 本文件
```

## 图表清单 (Figure List)

所有图表使用完整的3年数据集（约26,281个数据点，915天有效数据）。

| 图号 | 名称 | 说明 |
|------|------|------|
| Fig 1 | 进水时间序列（CV对比，r=0.6）— 同时可视化 | 小/典型/大CV的COD/TSS在同一图对比 |
| Fig 1 new | 进水时间序列（CV对比，r=0.6）— 分开可视化 | 每个CV单独一行，展示COD和TSS |
| Fig 2 | 进水分布直方图（CV对比，r=0.6） | 小/典型/大CV的COD/TSS分布 |
| Fig 3 | 出水时间序列（r对比）— 同时可视化 | r=0/0.3/0.6/0.9的COD/TSS在同一图对比 |
| Fig 3 new | 出水时间序列（r对比）— 分开可视化 | 每个r单独一行，展示COD和TSS |
| Fig 4 | 出水分布直方图（r对比） | r=0/0.3/0.6/0.9的COD/TSS分布 |
| Fig 5 | 超标概率CCDF | COD/TSS/污泥TSS的超标概率曲线 |
| Fig 6 | 自相关函数ACF | 出水COD/TSS的ACF分析 |
| Fig 7 | 箱线图对比 | 不同r值的出水COD/TSS分布箱线图 |
| Fig 8 | 超标率柱状图 | 不同r值的COD/TSS超标率对比 |
| Fig 9 | 污泥产量（r对比）— 同时可视化 | 污泥TSS时间序列和分布（所有r在同一图） |
| Fig 9 new | 污泥产量（r对比）— 分开可视化 | 每个r单独一行，展示TSS和流量（合并原Fig 14） |
| Fig 10 | 污泥综合分析（流量/TSS/产率）— 同时可视化 | 所有r在同一图对比 |
| Fig 10 new | 污泥综合分析— 分开可视化 | 每个r单独一行，展示流量、TSS和产率直方图 |
| Fig 11 | 需氧量分析— 同时可视化 | 所有r在同一图对比 |
| Fig 11 new | 需氧量分析— 分开可视化 | 每个r单独一行，展示时间序列和直方图 |
| Fig 12 | 进水ACF和分布（r对比） | 进水COD的ACF和分布直方图 |
| Fig 13 | 出水时间序列（CV对比）— 同时可视化 | 不同CV的出水COD/TSS在同一图 |
| Fig 13 new | 出水时间序列（CV对比）— 分开可视化 | 每个CV单独一行，展示COD和TSS |

## 图表命名规则

- `fig[N]_[description].png` — 同时可视化版本（多条曲线在同一图）
- `fig[N]_[description]_separate.png` — 分开可视化版本（每个参数单独一行子图）

## 数据说明

- **数据时长**: 3年（1095天）
- **采样频率**: 每小时一个数据点
- **总数据点**: 每个文件约26,281个数据点
- **预热期**: 前180天数据被排除在分析之外
- **有效数据**: 约915天（26,000+ 数据点）

## 运行方式

```bash
cd /home/amoris/ese5880c-project2

# 转换数据（如需要）
python3 scripts/convert_xlsx.py

# 运行分析
python3 scripts/analysis.py
```

## 输出文件

- `output/figures/` — 18张PNG图表（300 DPI）
- `output/summary.md` — 完整分析报告
- `output/aor_table.md` — 需氧量汇总表
- `output/parameter_validation.md` — 参数验证报告

## 依赖项

- Python 3.8+
- numpy
- matplotlib
- scipy
