# FEM

## Overview
This repository contains a numerical solution of the following differencial equation.

### Governing Equation
$$
-\frac{d}{dx}\left(E(x)\frac{du(x)}{dx}\right) = -1000 \sin(\pi x)
$$

### Boundary Conditions
$$
\begin{aligned}
\text{Dirichlet (Right):} \quad & u(2) = 3 \\
\text{Cauchy/Robin (Left):} \quad & \frac{du(0)}{dx} + 2u(0) = 10
\end{aligned}
$$

### Material Properties
$$
E(x) = \begin{cases} 
2 & \text{for } x \in [0, 1] \\ 
6 & \text{for } x \in (1, 2] 
\end{cases}
$$
