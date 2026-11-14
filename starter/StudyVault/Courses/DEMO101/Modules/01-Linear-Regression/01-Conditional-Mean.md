---
type: concept
course: DEMO101
aliases:
  - Conditional mean
---

# Conditional mean

同一个 predictor value $x$ 可以对应许多不同的 response values。Simple linear regression 用一条直线描述它们的 conditional mean。

## Mean model

$$
Y_i=\beta_0+\beta_1 x_i+\varepsilon_i,
\qquad
\operatorname{E}(\varepsilon_i\mid X)=0.
$$

给定 design matrix $X$，第 $i$ 个 response 的 conditional mean 是 $\beta_0+\beta_1x_i$。Population parameter $\beta_1$ 描述 $x$ 每增加一个单位时，conditional mean 的变化。 ^conditional-mean

如果 $\beta_0=2$，$\beta_1=1.5$，那 $x=4$ 对应的 conditional mean 是 $8$。各个 observations 仍可围绕 $8$ 上下波动，这部分留给 [[Courses/DEMO101/Modules/01-Linear-Regression/03-Constant-Variance|constant variance]] 描述。

## Find it in the lecture

![[Courses/DEMO101/Materials/Slides/L01-Regression-Diagnostics.pdf#page=1&height=340]]

- [[Courses/DEMO101/Materials/Sources/L01|L01 source and page map]]
- [[Courses/DEMO101/Practice/Worksheets/Worksheet-01#Q01|Worksheet 01 · Q01]]
- [[Courses/DEMO101/Modules/01-Linear-Regression/Module|Module outline]]
