---
type: lab
course: DEMO101
---

# Variance lab

[[Courses/DEMO101/Modules/01-Linear-Regression/03-Constant-Variance|Constant variance]]

Move **Spread growth κ** from 0 to 2.4. Compare the spread of observations around the fitted line with the spread of residuals around zero. Hover over a point to find the same observation in the other plot.

## Interactive demo

Open `index.html` from this folder in a desktop browser. The plots work offline.

To interact with the plots inside Obsidian, run this command from the `StudyVault` directory and switch the note to Reading view.

```bash
cd Courses/DEMO101/Labs/variance
python3 -m http.server 8765 --bind 127.0.0.1
```

<iframe src="http://127.0.0.1:8765/index.html" title="Interactive variance lab" width="100%" height="720"></iframe>

[Open the running lab in a browser](http://127.0.0.1:8765/index.html). Press Ctrl+C in the Terminal to stop the server.

## Model

For each fixed predictor value $x_i \in [0,1]$, the demonstration uses the same fixed standardized disturbance $z_i$ at every slider setting:

$$
y_i = 1 + 2x_i + (0.24 + \kappa x_i)z_i.
$$

The simulator refits OLS with an intercept each time $\kappa$ changes and draws $e_i=y_i-\hat y_i$ against $\hat y_i$. For hypothetical independent $Z_i$ with mean 0 and variance 1, the corresponding model has $\operatorname{Var}(Y_i\mid x_i)=(0.24+\kappa x_i)^2$. The fixed disturbances keep the comparison focused on changing spread.

## Offline reference

![[Courses/DEMO101/Materials/Images/Variance-Comparison.png]]

As spread increases with the predictor, the residual plot tends to fan out. A single simulated sample can have uneven spread even when $\kappa=0$.
