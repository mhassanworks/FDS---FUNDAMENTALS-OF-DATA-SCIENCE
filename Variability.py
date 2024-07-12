import numpy as np
from scipy import stats

data = [10, 20, 30, 40, 50]

# Range
data_range = np.ptp(data)
print("Range:", data_range)

# Variance
variance = np.var(data)
print("Variance:", variance)

# Standard Deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Interquartile Range (IQR)
iqr = stats.iqr(data)
print("Interquartile Range (IQR):", iqr)
