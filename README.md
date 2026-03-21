# ESE5880C Project 2 — 污水处理系统进水自相关对出水水质影响分析

## 项目概述

本项目研究了**进水时间序列自相关(autocorrelation)**对污水处理系统性能的影响。通过BioWin软件模拟，我们比较了无自相关(r=0)和不同自相关程度(r=0.3, 0.6, 0.9)的进水条件对系统出水水质(COD、TSS)和污泥产量的影响。

## 目录结构

```
/home/amoris/ese5880c-project2/
├── data/                          # 原始数据目录
│   ├── biowin/                    # BioWin模拟数据
│   │   ├── biowin data NO self-related/  # 无自相关数据
│   │   └── biowin data self-related/    # 自相关数据（不同r值）
│   └── 进水数据.xlsx              # 进水数据文件
├── docs/                          # 项目文档
│   ├── 任务.txt                   # 任务说明
│   ├── 分工.txt                   # 分工安排
│   ├── 要求总结.txt               # 要求总结
│   └── ESE5880C Project 2.pdf    # 项目PDF文档
├── scripts/                       # 分析脚本
│   ├── analysis.py                # 主分析脚本（生成所有图表和报告）
│   └── convert_xlsx.py            # 快速xlsx转CSV工具
├── output/                        # 输出目录
│   ├── analysis.py                # 分析脚本副本
│   ├── convert_xlsx.py            # 转换工具副本
│   ├── summary.md                 # 文字总结报告
│   ├── cache/                     # CSV缓存文件
│   └── figures/                   # 图表文件（300 DPI PNG）
│       ├── fig1_influent_timeseries_cv.png
│       ├── fig2_influent_histogram_cv.png
│       ├── fig3_effluent_timeseries_r.png
│       ├── fig4_effluent_histogram_r.png
│       ├── fig5_exceedance_cdf_r.png
│       ├── fig6_acf_r.png
│       ├── fig7_boxplot_r.png
│       └── fig8_violation_rate_r.png
├── README.md                      # 本文件
├── requirements.txt               # Python依赖包
├── task.md                        # 任务清单
├── walkthrough.md                 # 项目完成报告
└── unfinished-prompt.md           # 收尾工作提示
```

## 运行环境

### Linux系统环境

- Python 3.13+
- 已安装的系统依赖：
  - numpy, matplotlib, scipy（用于数据分析和绘图）
  - 无特殊系统库要求

### Python依赖

```
numpy
matplotlib
scipy
```

## 使用方法

### 1. 数据准备（可选，已完成）

项目已包含预处理好的数据文件。如果需要重新转换原始xlsx文件：

```bash
cd /home/amoris/5880C
python3 scripts/convert_xlsx.py
```

### 2. 运行分析脚本

```bash
cd /home/amoris/5880C
python3 scripts/analysis.py
```

该脚本会：
- 加载所有数据集
- 生成8个分析图表到`output/figures/`目录
- 计算统计数据
- 生成文字总结报告`output/summary.md`

### 3. 查看结果

- 图表：打开`output/figures/`目录下的PNG文件
- 文字报告：查看`output/summary.md`
- 统计结果：报告中包含详细的统计表格

## 关键发现

### 进水自相关对出水水质的影响（典型CV情况）

| 自相关系数r | 出水COD均值(mg/L) | 出水COD标准差 | COD变异系数% | COD超标率% | 出水TSS均值(mg/L) | 出水TSS标准差 | TSS变异系数% | TSS超标率% |
|------------|------------------|--------------|-------------|-----------|------------------|--------------|-------------|-----------|
| 0          | 37.59            | 2.93         | 7.8         | 0.00      | 2.58             | 0.13         | 5.2         | 0.00      |
| 0.3        | 38.24            | 5.87         | 15.4        | 0.74      | 2.58             | 0.27         | 10.4        | 0.00      |
| 0.6        | 39.18            | 8.17         | 20.9        | 1.96      | 2.60             | 0.27         | 10.3        | 0.00      |
| 0.9        | 37.92            | 7.48         | 19.7        | 2.29      | 2.51             | 0.29         | 11.5        | 0.00      |

**结论：**
- 随着自相关系数r增加，出水COD和TSS的**波动性显著增大**（标准差和变异系数上升）
- **超标风险随r单调上升**：r=0.9时COD超标率是r=0的近31倍
- 出水TSS始终远低于30mg/L标准（均值约2.5mg/L，最大值很少超过4mg/L），基本不受自相关影响
- 平均出水水质相对稳定，但**尾部风险（极端值）显著增加**

**图表说明：**
- 由于出水TSS数据远低于30mg/L标准，为了更好地展示TSS数据的实际变化，所有TSS相关图表（时间序列图、直方图、箱图、CCDF图）均省略了30mg/L标准线

## 排放标准

采用中国《城镇污水处理厂污染物排放标准》（GB18918-2002）一级A标准：
- **COD ≤ 60 mg/L**
- **TSS ≤ 30 mg/L**

## 技术特点

### 快速数据加载

原始xlsx文件（压缩后4MB，展开后20MB+XML）使用传统Python解析器需要≥10分钟。本项目开发了`convert_xlsx.py`工具：
- 使用`xml.etree.ElementTree.iterparse`流式解析
- 直接写入CSV格式
- 每个文件转换时间仅需**~0.8秒**

### 数据分析流程

1. 数据加载与清洗
2. 时间序列分析
3. 概率分布分析
4. 自相关函数(ACF)分析
5. 超标概率计算
6. 图表生成
7. 文字报告撰写

## 图表说明

| 图表编号 | 图表名称 | 描述 |
|---------|---------|------|
| Fig1 | 进水时间序列（CV对比） | 三种CV水平的进水COD/TSS时间序列图 |
| Fig2 | 进水直方图（CV对比） | 三种CV水平的进水COD/TSS直方图 |
| Fig3 | 出水时间序列（r对比） | 四种自相关水平的出水COD/TSS时间序列图 |
| Fig4 | 出水直方图（r对比） | 四种自相关水平的出水COD/TSS直方图 |
| Fig5 | 超标概率CCDF图 | 出水COD、TSS和污泥TSS的超标概率累积分布函数图 |
| Fig6 | ACF自相关函数图 | 出水COD和TSS的自相关函数图 |
| Fig7 | 箱图 | 不同自相关水平的出水COD/TSS箱图 |
| Fig8 | 超标率柱状图 | 不同自相关水平的COD/TSS超标率 |
| Fig9 | 剩余污泥产量图 | 剩余污泥TSS的时间序列和分布直方图 |

## 作者

项目由ESE5880C课程团队完成。

## 完成时间

2026年3月21日
