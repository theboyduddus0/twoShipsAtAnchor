import sympy as sp
import time

# Start time
start_time = time.time()
# Define general boat coordinates
x_a, y_a = sp.symbols('x_a y_a')  # Ship A coordinates
x_b, y_b = sp.symbols('x_b y_b')  # Ship B coordinates

# Define x as a symbolic variable
x = sp.Symbol('x')

# Define a general function f(x) for the shoreline
f = sp.Function('f')(x)  # f(x) represents a general function

# Define the total distance function D
D = sp.sqrt((x - x_a)**2 + (y_a - f)**2) + sp.sqrt((x_b - x)**2 + (y_b - f)**2)

# Compute the derivative D' w.r.t x
D_prime = sp.diff(D, x)

# simplify the  first derivative
sp.simplify(D_prime)

print(f'\ndD/dx = {D_prime}')

# Compute the second derivative D'' w.r.t x
D_doublePrime = sp.diff(D_prime, x)

# simplify the second derivative
sp.simplify(D_doublePrime)

print(f'\nd^2D/dx^2 = {D_doublePrime}')

end_time = time.time()
execution_time = end_time - start_time

# Print execution time
print(f"\nExecution time: {execution_time:.4f} seconds")
