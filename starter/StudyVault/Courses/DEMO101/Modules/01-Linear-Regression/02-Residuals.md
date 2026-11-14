---
type: concept
course: DEMO101
aliases:
  - Residuals
---

# Residuals

Residual 是观测值与该样本的 fitted value 之间的差。它用同一批 observations 估计出来的 fitted line 作为基准。

## Definition

$$
e_i=y_i-\hat y_i,
\qquad
\hat y_i=\hat\beta_0+\hat\beta_1x_i.
$$

例如 $y_i=8.6$ 且 $\hat y_i=7.9$ 时，$e_i=0.7$。Population error $\varepsilon_i$ 则以未知的 [[Courses/DEMO101/Modules/01-Linear-Regression/01-Conditional-Mean#Mean model|conditional mean]] 为基准。

在 residual plot 中，将 $\hat y_i$ 作为横轴、$e_i$ 作为纵轴。检查中心附近是否弯曲，也查看垂直散布是否随横轴变化。

- [[Courses/DEMO101/Modules/01-Linear-Regression/03-Constant-Variance|Constant variance]]
- [[Courses/DEMO101/Practice/Exams/Practice-Exam-01#Q01|Practice Exam 01 · Q01]]
- [[Courses/DEMO101/Modules/01-Linear-Regression/Module|Module outline]]
