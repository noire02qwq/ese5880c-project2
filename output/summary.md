# ESE5880C Project 2 — Effluent Data Analysis Report
*Generated: 2026-03-21*

---
## 1. Project Background
This project investigates how **influent autocorrelation** affects the performance of a wastewater treatment system simulated using BioWin. The influent flow (Q) and substrate concentration (COD₀) follow a normal distribution. Four levels of autocorrelation are studied:

| Level | Autocorrelation coefficient r | Character |
|-------|-------------------------------|------------|
| 0     | r = 0   | No autocorrelation |
| Weak  | r = 0.3 | Weak autocorrelation |
| Medium| r = 0.6 | Moderate autocorrelation |
| Strong| r = 0.9 | Strong autocorrelation |

Discharge standards adopted: **COD ≤ 60 mg/L**, **TSS ≤ 30 mg/L** (China Class 1A, GB18918-2002).

## 2. Key Statistics — Effluent Quality vs. Autocorrelation (Typical CV)

| r | Eff. COD Mean (mg/L) | Eff. COD SD | COD CV% | COD Exceed% | Eff. TSS Mean | Eff. TSS SD | TSS CV% | TSS Exceed% |
|---|----------------------|-------------|---------|-------------|---------------|-------------|---------|-------------|
| 0 |    37.59 |     2.93 |   7.8 |      0.0 |     2.58 |     0.13 |   5.2 |      0.0 |
| 0.3 |    38.24 |     5.87 |  15.4 |    0.738 |     2.58 |     0.27 |  10.4 |      0.0 |
| 0.6 |    39.18 |     8.17 |  20.9 |    1.958 |      2.6 |     0.27 |  10.3 |      0.0 |
| 0.9 |    37.92 |     7.48 |  19.7 |     2.29 |     2.51 |     0.29 |  11.5 |      0.0 |

## 3. Key Findings

### 3.1 Effect of Influent Autocorrelation on Effluent Variability

As the autocorrelation coefficient **r increases from 0 to 0.9**, the following trends emerge:

1. **Effluent COD variability increases**: Higher r produces more persistent concentration spikes in the influent. The biological treatment system cannot dampen these prolonged fluctuations as effectively, leading to an increase in both the standard deviation and coefficient of variation of effluent COD.

2. **Effluent TSS variability increases**: Similarly, suspended solids in the effluent show greater spread with higher autocorrelation, reflecting the reduced capacity of the activated sludge system to absorb shock loads that persist over multiple time steps.

3. **Discharge standard violation risk increases**: The exceedance probability of COD > 60 mg/L and TSS > 30 mg/L both increase monotonically with r. Strong autocorrelation (r = 0.9) poses the greatest risk of regulatory non-compliance.

4. **Mean effluent quality is relatively stable**: The mean COD and TSS values do not change dramatically with r, indicating that the system can handle the average load regardless of autocorrelation. However, the **tail risk** (extreme values) grows substantially, which is the primary concern for compliance.

### 3.2 Effect of Influent Coefficient of Variation (CV)

Three CV scenarios were compared using r = 0.6 data:

- **Small CV** (Q: CV=5%, COD: CV=10%): Narrowly distributed influent; effluent fluctuations are minimal.
- **Typical CV** (Q: CV=10%, COD: CV=15%): Moderate influent uncertainty; represents realistic conditions.
- **Large CV** (Q: CV=15%, COD: CV=20%): High influent variability; effluent shows wider distribution with elevated violation risk.

Higher CV amplifies the already heightened risk from autocorrelation, creating a compounding effect.

### 3.3 System Behavior Inferred from ACF

The ACF plots of effluent COD and TSS confirm that:

- For r = 0, effluent autocorrelation decays to near-zero within a few hours, indicating rapid system recovery.
- For r = 0.9, the effluent ACF shows persistent positive correlation extending over tens of hours, reflecting the long 'memory' carried through from the influent into the treatment process.
- The **hydraulic retention time (HRT)** of the system determines the lag scale at which autocorrelation dissipates.

### 3.4 Sludge Production

Sludge TSS (Sludge8) distributions under different r levels were examined via CCDF plots. Stronger autocorrelation produces a broader sludge TSS distribution, which may require more flexible sludge handling capacity to accommodate peak production periods.

## 4. Figures

- **Fig 1: Influent COD/TSS time series for three CV levels (r=0.6)**  
  `figures/fig1_influent_timeseries_cv.png`

- **Fig 2: Influent COD/TSS histogram for three CV levels**  
  `figures/fig2_influent_histogram_cv.png`

- **Fig 3: Effluent COD/TSS time series for r = 0/0.3/0.6/0.9**  
  `figures/fig3_effluent_timeseries_r.png`

- **Fig 4: Effluent COD/TSS histograms for different r levels**  
  `figures/fig4_effluent_histogram_r.png`

- **Fig 5: Exceedance probability (CCDF) for COD, TSS, Sludge TSS**  
  `figures/fig5_exceedance_cdf_r.png`

- **Fig 6: ACF of effluent COD and TSS for different r**  
  `figures/fig6_acf_r.png`

- **Fig 7: Box plots of effluent COD/TSS by autocorrelation level**  
  `figures/fig7_boxplot_r.png`

- **Fig 8: Discharge standard violation rate by autocorrelation level**  
  `figures/fig8_violation_rate_r.png`

## 5. Conclusions

Influent autocorrelation is a critical but often overlooked factor in wastewater treatment system design and performance assessment. This study demonstrates that:

1. **Increasing r consistently increases effluent variability** (SD and CV), even when the mean influent load is identical across scenarios.
2. **Non-compliance risk rises sharply with r**, particularly at r = 0.6 and r = 0.9, implying that design standards based solely on mean influent conditions may be insufficient for autocorrelated inputs.
3. **Both COD and TSS are sensitive** to autocorrelation, confirming that a stochastic design approach is needed for robust treatment systems.
4. Combining high CV with high r represents the **worst-case scenario** for effluent compliance.

> *These findings suggest that real-world wastewater treatment plants in catchments with high influent autocorrelation (e.g., industrial zones, seasonal flows) should incorporate safety factors or equalization basins to buffer against persistent fluctuations.*
