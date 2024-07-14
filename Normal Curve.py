import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 0
std_dev = 1

# Generate data points
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)
y = norm.pdf(x, mean, std_dev)

# Create the plot
plt.plot(x, y, label='Normal Distribution')

# Add title and labels
plt.title('Normal Distribution Curve')
plt.xlabel('X-axis')
plt.ylabel('Probability Density')

# Show legend
plt.legend()

# Show the plot
plt.show()
