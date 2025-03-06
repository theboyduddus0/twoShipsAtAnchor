import numpy as np
import matplotlib.pyplot as plt

# Ship coordinates
x_a, y_a = 2, 6  # Ship A
x_b, y_b = 8, 8  # Ship B


# Define the shoreline function
def f(x):
    return 3 * np.sin(x)  # Now f(x) is a function

def g(x):
    return 1/3 * x**2 - 3*x + 2


# optimal landing spot for sin function
x_p = 1.74170871156415
y_p = f(x_p)

# optimal landing spot for quadratic function
x_q = 10.3154918119950
y_q = g(x_q)


# Generate x values for plotting shorelines
x_vals = np.linspace(-2, 11, 200)
y_f = f(x_vals)  # First shoreline
y_g = g(x_vals)  # Second shoreline

# Plot setup
plt.figure(figsize=(8, 6))

# Plot ships and landing points
plt.scatter([x_a, x_b, x_p, x_q], [y_a, y_b, y_p, y_q],
            color=['blue', 'red', 'green', 'purple'])

# Annotate points
plt.text(x_a, y_a, "boat A", fontsize=12, verticalalignment='bottom', color='blue')
plt.text(x_b, y_b, "boat B", fontsize=12, verticalalignment='bottom', color='red')
plt.text(x_p, y_p, " P1", fontsize=12, verticalalignment='top', color='green')
plt.text(x_q, y_q, " P2", fontsize=12, verticalalignment='top', color='purple')


# Plot paths for shoreline f(x)
plt.plot([x_a, x_p], [y_a, y_p], 'b--')
plt.plot([x_b, x_p], [y_b, y_p], 'r--')

# Plot paths for shoreline f(x)
plt.plot([x_a, x_q], [y_a, y_q], 'b--')
plt.plot([x_b, x_q], [y_b, y_q], 'r--')

# Plot shorelines
plt.plot(x_vals, y_f, 'k-', label="Shoreline $f(x)$")
plt.plot(x_vals, y_g, 'k-', label="Shoreline $g(x)$")


# Labels and legend
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.title("Optimised path for two functional shorelines")
plt.legend()
plt.grid()
plt.savefig('figures/pathToTake.png')
