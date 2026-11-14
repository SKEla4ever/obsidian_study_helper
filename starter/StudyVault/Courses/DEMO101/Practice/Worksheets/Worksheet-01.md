---
type: worksheet
course: DEMO101
week: 1
---

# Worksheet 01 · Assumptions

参考资料 [[Courses/DEMO101/Materials/Sources/L01|L01 · Regression diagnostics]]。

## Q01

在 simple linear regression model 中，$\beta_0=2$，$\beta_1=1.5$。给定 $x=4$ 时，求 conditional mean。

知识点 · [[Courses/DEMO101/Modules/01-Linear-Regression/01-Conditional-Mean|Conditional mean]]

> [!success]- Solution
> $\operatorname{E}(Y\mid x=4)=2+1.5\times4=8$。

## Q02

如果 residual plot 中的点都围绕零分布，但垂直散布随 fitted values 变大，应该首先复查哪条 assumption？

知识点 · [[Courses/DEMO101/Modules/01-Linear-Regression/03-Constant-Variance|Constant variance]]

Q02 #review/missed

> [!success]- Solution
> 先复查 constant variance。将 fitted values 较小与较大的区域分开，比较 residuals 的垂直散布。
>
> 如果右侧的散布持续更宽，样本形状提示可能存在 heteroscedasticity。[[Courses/DEMO101/Labs/variance/Lab|Variance lab]] 可以重现这种变化。

[[Courses/DEMO101/Practice/Practice|Practice index]]
