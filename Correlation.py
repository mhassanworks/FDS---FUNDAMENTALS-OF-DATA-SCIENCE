import pandas as pd
import numpy as np

# Sample data
data = {
    'variable1': [1, 2, 3, 4, 5],
    'variable2': [2, 4, 6, 8, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Print the correlation matrix
print(correlation_matrix)

# Calculate the correlation coefficient between two specific variables
correlation_coefficient = np.corrcoef(df['variable1'], df['variable2'])[0, 1]
print(f'Correlation coefficient between variable1 and variable2: {correlation_coefficient}')
