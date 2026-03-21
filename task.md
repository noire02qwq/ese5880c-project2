# ESE5880C Project 2 - 出水数据分析任务

## Phase 1: 数据探索与规划
- [x] 阅读项目描述文件（任务.txt、分工.txt、要求总结.txt）
- [x] 检查目录结构和所有数据文件
- [x] 了解xlsx文件列结构（共17列）
- [x] 制定实施计划

## Phase 2: 目录结构规范化
- [x] 在 /home/amoris/5880C 下创建 output/ 目录

## Phase 3: 数据加载与预处理
- [x] 编写快速自定义xlsx解析器（绕过pandas缓慢加载问题）
- [x] 加载 "no self-related" 出水数据（r=0）
- [x] 加载 "typical" CV 的三个自相关组（r=0.3, 0.6, 0.9）
- [x] 加载 "small" 和 "large" CV 的自相关 r=0.6 组（用于CV比较）
- [x] 数据清洗和单位整理

## Phase 4: 绘图（Part 1 - 不同CV的影响）
- [x] 图1: 进水COD/TSS 时间序列（三种CV，无自相关）
- [x] 图2: 进水COD/TSS 的 Histogram（三种CV）

## Phase 5: 绘图（Part 2 - 不同自相关r的影响，典型CV）
- [x] 图1: 出水COD、TSS 时间序列图（4种r）
- [x] 图2: histogram（4种r）
- [x] 图3: 超标概率 CDF 图（出水COD、TSS、剑余污泥）
- [x] 图4: ACF图（四个情况一个图）
- [x] 图5: 筱图，对比不同自相关的均値和标准差
- [x] 图6: 超标比例柱状图

## Phase 6: 文字总结
- [x] 撰写文字总结报告 (output/summary.md)

## Phase 7: 整理输出
- [x] 所有图表存入 output/figures/
- [x] 总结文档 output/summary.md
- [x] 生成分析脚本 output/analysis.py + output/convert_xlsx.py

## Phase 4: 绘图（Part 1 - 不同CV的影响）
- [ ] 图1: 进水COD/TSS 时间序列（三种CV，无自相关）
- [ ] 图2: 进水COD/TSS 的 Histogram（三种CV）

## Phase 5: 绘图（Part 2 - 不同自相关r的影响，典型CV）
- [ ] 图1: 出水COD、TSS 时间序列图（4种r：0/0.3/0.6/0.9）
  - 标注排放标准线（COD 60 mg/L，TSS 30 mg/L）
- [ ] 图2: 出水COD、TSS Histogram（4种r）
- [ ] 图3: 超标概率 CDF 图（出水COD、TSS，包括Sludge参数）
- [ ] 图4: ACF 自相关函数图（4种情况合并一图）
- [ ] 图5: 箱图（对比不同自相关的均值和标准差）
- [ ] 图6: 进出水Q和COD对比（波动衰减，optional）

## Phase 6: 文字总结
- [ ] 撰写英文或中英双语总结报告（Markdown格式）
- [ ] 总结关键发现（自相关对出水波动、超标风险的影响）

## Phase 7: 整理输出
- [ ] 所有图表存入 output/figures/
- [ ] 总结文档存入 output/summary.md
- [ ] 生成分析脚本 output/analysis.py
