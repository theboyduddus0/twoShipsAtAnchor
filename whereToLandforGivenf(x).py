import sympy as sp

# Ship coordinates
x_a, y_a = 2, 6  # Ship A
x_b, y_b = 8, 8  # Ship B

# Define symbols
x = sp.Symbol('x')

# Define the shoreline function
f_x = 3*sp.sin(x)

f_x = 1/3 * x**2 - 3*x + 2

# Form the distance equation
D = sp.sqrt((x-x_a)**2 + (y_a-f_x)**2) + sp.sqrt((x_b-x)**2 + (y_b-f_x)**2)

# Differentiate with respect to x_p
D_prime = sp.diff(D, x)
x_p = sp.nsolve(D_prime, x, 10)

print(f'\nOptimum x coordinate to use: x_p =  {x_p}')
