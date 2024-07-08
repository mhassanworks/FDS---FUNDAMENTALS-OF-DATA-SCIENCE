import collections
import matplotlib.pyplot as plt

# Example data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Create frequency distribution
frequency_distribution = collections.Counter(data)

# Print frequency distribution
print(frequency_distribution)

# Plot frequency distribution
plt.bar(frequency_distribution.keys(), frequency_distribution.values())
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Frequency Distribution')
plt.show()
