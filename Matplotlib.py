import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a plot
plt.plot(x, y, label='Sample Data', marker='o')

# Add titles and labels
plt.title('Basic Plot Example')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# Show legend
plt.legend()

# Display the plot
plt.show()
