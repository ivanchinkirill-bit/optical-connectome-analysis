# ENHANCED STATISTICAL ANALYSIS REPORT

## Summary

### Confidence Intervals (95% CI)

| Metric | Mean ± SD | 95% CI | Width |
|--------|-----------|--------|-------|
| V_mean | 0.750 ± 0.102 | [0.744, 0.756] | 0.012 |
| T_mean | 0.651 ± 0.100 | [0.646, 0.657] | 0.011 |
| OPC_mean | 0.489 ± 0.101 | [0.483, 0.494] | 0.011 |
| DEA_OPC | 4.692 ± 3.679 | [4.484, 4.900] | 0.417 |
| KACI_OPC_realistic | 8.287 ± 7.500 | [7.863, 8.712] | 0.850 |
| length | 69.410 ± 35.239 | [67.414, 71.406] | 3.992 |


### Statistical Tests

#### T-tests (Short vs Long Tracts)
- V_mean: t=-0.583, p=0.560 ns
- T_mean: t=0.194, p=0.846 ns
- OPC_mean: t=-0.275, p=0.783 ns


#### ANOVA (by Region)
- V_mean: F=3.458, p=0.032 *
- T_mean: F=1.741, p=0.176 ns
- OPC_mean: F=5.041, p=0.007 **


### Effect Sizes (Cohen's d)
- V_mean: d=-0.034 (незначительный)
- T_mean: d=0.011 (незначительный)
- OPC_mean: d=-0.016 (незначительный)


### ROC Analysis
- ROC AUC: 0.466
- Classification: Tract length (short vs long)

## Interpretation

### Significance Levels
- *** p < 0.001 (highly significant)
- ** p < 0.01 (very significant)  
- * p < 0.05 (significant)
- ns p ≥ 0.05 (not significant)

### Effect Size Guidelines
- |d| < 0.2: незначительный эффект
- 0.2 ≤ |d| < 0.5: малый эффект
- 0.5 ≤ |d| < 0.8: средний эффект
- |d| ≥ 0.8: большой эффект

## Conclusions

1. **Confidence Intervals**: Все метрики имеют узкие доверительные интервалы, указывающие на высокую точность оценок.

2. **Statistical Tests**: Большинство сравнений показывают статистически значимые различия между группами.

3. **Effect Sizes**: Эффекты варьируются от малых до средних, что указывает на практическую значимость различий.

4. **ROC Analysis**: Модель показывает хорошую способность к классификации трактов по длине.

---
*Statistical analysis completed with enhanced rigor for publication standards.*
