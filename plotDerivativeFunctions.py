import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define x as a symbolic variable
x = sp.Symbol('x')
# Given function
f = 3*sp.sin(x)

# Given Co-ordinates
x_a, y_a = 2, 6
x_b, y_b = 8, 8

# Define the total distance function D
D = sp.sqrt((x - x_a)**2 + (y_a - f)**2) + sp.sqrt((x_b - x)**2 + (y_b - f)**2)

# Compute the derivative D' w.r.t x
D_prime = sp.diff(D, x)

# Convert the symbolic first derivative to a numerical function
D_prime_func = sp.lambdify(x, D_prime, modules=["numpy"])

# Compute second derivative d²D/dx²
D_doublePrime = sp.diff(D_prime, x)

# Convert the symbolic second derivative to a numerical function
D_doublePrime_func = sp.lambdify(x, D_doublePrime, modules=["numpy"])

# Define x-values over which to evaluate the derivative
x_values = np.linspace(-8, 14, 500)
y_prime_values = D_prime_func(x_values)   # Compute dD/dx
y_double_prime_values = D_doublePrime_func(x_values)  # Compute d²D/dx²


# Plot the derivative function
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_prime_values, label=r"First Derivative $\frac{dD}{dx}$", color='b')
plt.plot(x_values, y_double_prime_values, label=r"Second Derivative $\frac{d^2D}{dx^2}$", color='r', linestyle="--")
plt.axhline(0, color='gray', linestyle='--')  # Horizontal reference line
plt.axhline(0, color='gray', linestyle='--')  # Add horizontal line at y=0
plt.xlabel("x")
plt.ylabel(r"Rate of Change of Total Distance $\frac{dD}{dx}$")
plt.title("Derivative of the Total Distance Function")
plt.legend()
plt.grid()
plt.savefig('figures/DerivativeFunctionPlots')
