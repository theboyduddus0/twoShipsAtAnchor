import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define x as a symbolic variable
x = sp.Symbol('x')

# Given function f(x)
f = 3 * sp.sin(x)

# Alternative function
f = 1/3 * x**2 - 3*x + 2

# Given coordinates
x_a, y_a = 2, 6
x_b, y_b = 8, 8

# Define the total distance function D
D = sp.sqrt((x - x_a)**2 + (y_a - f)**2) + sp.sqrt((x_b - x)**2 + (y_b - f)**2)

# Convert the symbolic function D(x) to a numerical function
D_func = sp.lambdify(x, D, modules=["numpy"])

# Define x-values over which to evaluate the function
x_values = np.linspace(-6, 12, 800)  # 400 points from x=0 to x=10
D_values = D_func(x_values)   # Compute D(x)

# Plot the distance function
plt.figure(figsize=(8, 5))
plt.plot(x_values, D_values, label=r"Total Distance $D(x)$", color='g')
plt.xlabel("x (Landing Point)")
plt.ylabel("Total Travel Distance D(x)")
plt.title("Total Distance as a Function of Landing Point")
plt.legend()
plt.grid()
plt.savefig('figures/DistanceFunctionPlot.png')
