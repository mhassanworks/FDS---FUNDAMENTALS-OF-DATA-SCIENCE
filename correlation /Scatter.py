import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Example data
x = np.random.rand(100)
y = 2 * x + np.random.randn(100) * 0.1

# Calculate correlation coefficient
correlation, _ = pearsonr(x, y)
print(f'Correlation coefficient: {correlation}')

# Create scatter plot
plt.scatter(x, y, label=f'Correlation: {correlation:.2f}')
plt.title('Scatter Plot with Correlation Coefficient')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
