import matplotlib.pyplot as plt

# Example Ship coordinates
x_a, y_a = 2, 4  # Ship A
x_b, y_b = 8, 3  # Ship B

# Compute the optimal landing point 1
x_p1 = (x_a * y_b + x_b * y_a) / (y_a + y_b)

# Compute optimal landing point 2
x_p2 = (-x_a*y_b + x_b*y_a)/(y_a - y_b)

y_p = 0  # Shoreline is at y = 0

# Below is the optimum
x_p = x_p1

# Plot setup
plt.figure(figsize=(8, 6))

# Plot ships and landing point
plt.scatter([x_a, x_b, x_p], [y_a, y_b, y_p], color=['blue', 'red', 'green'], label="Ships & Landing")
plt.text(x_a, y_a, " A", fontsize=12, verticalalignment='bottom', color='blue')
plt.text(x_b, y_b, " B", fontsize=12, verticalalignment='bottom', color='red')
plt.text(x_p, y_p, " p", fontsize=12, verticalalignment='top', color='green')

# Plot paths
plt.plot([x_a, x_p], [y_a, y_p], 'b--', label="A to Landing")
plt.plot([x_b, x_p], [y_b, y_p], 'r--', label="B to Landing")

# Draw shoreline
plt.axhline(0, color='black', linewidth=1, linestyle='-')

# Labels and legend
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
plt.title("Optimal Landing Point for Minimum Travel Distance")
plt.legend()
plt.grid()
plt.savefig('figures/pathForStraightShoreline.png')
