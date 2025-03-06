import sympy as sp

# Define symbols
x_a, y_a, x_b, y_b, x = sp.symbols('x_a y_a x_b y_b x')

# Form the total distance travelled equation
D = sp.sqrt((x-x_a)**2 + y_a**2) + sp.sqrt((x_b-x)**2 + y_b**2)

# Differentiate D with respect to x, our optimal landing point
D_prime = sp.diff(D, x)

# Set the derivative equal to zero (to find minimum/maximum) and solve for x
x_solutions = sp.solve(D_prime, x)

# Print the optimal landing points
for solution in x_solutions:
    print(f'\nPossible landing mark: x_p =  {solution}')
