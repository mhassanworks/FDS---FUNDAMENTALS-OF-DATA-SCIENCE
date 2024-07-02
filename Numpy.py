import numpy as np

# Creating NumPy arrays
arr_from_list = np.array([1, 2, 3, 4, 5])
arr_zeros = np.zeros((3, 3))
arr_ones = np.ones((2, 4))
arr_arange = np.arange(0, 10, 2)
arr_linspace = np.linspace(0, 1, 5)

print("Array from list:", arr_from_list)
print("Array of zeros:\n", arr_zeros)
print("Array of ones:\n", arr_ones)
print("Array using arange:", arr_arange)
print("Array using linspace:", arr_linspace)

# Basic operations
arr = np.array([1, 2, 3])
arr_sum = arr + 2
arr_prod = arr * 2

print("Original array:", arr)
print("Array after adding 2:", arr_sum)
print("Array after multiplying by 2:", arr_prod)

# Element-wise operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_add = arr1 + arr2
arr_mult = arr1 * arr2

print("Element-wise addition:", arr_add)
print("Element-wise multiplication:", arr_mult)

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_mult = np.dot(matrix1, matrix2)

print("Matrix multiplication result:\n", matrix_mult)

# Indexing and slicing
arr = np.array([1, 2, 3, 4, 5])
element = arr[0]
sub_array = arr[1:4]

print("First element:", element)
print("Sub-array from index 1 to 4:", sub_array)

# Reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshaped = arr.reshape((2, 3))

print("Original array:", arr)
print("Reshaped array to 2x3:\n", arr_reshaped)

# Aggregations
arr = np.array([1, 2, 3, 4, 5])
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)

print("Sum of array elements:", arr_sum)
print("Mean of array elements:", arr_mean)

# Finding elements
indices = np.where(arr > 3)

print("Indices where elements are greater than 3:", indices)
print("Elements greater than 3:", arr[indices])
