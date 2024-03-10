import numpy as np

# Creating a 1-dimensional NumPy array
array1d = np.array([1, 2, 3, 4, 5])

# Basic operations
addition_result = array1d + 10
subtraction_result = array1d - 3
multiplication_result = array1d * 2
division_result = array1d / 2
exponential_result = array1d ** 2
sqrt_result = np.sqrt(array1d)

# Indexing and slicing
print(array1d[0])  # Accessing the first element
print(array1d[1:4])  # Slicing from index 1 to 3

# Manipulating arrays
reshaped_array = np.reshape(array1d, (5, 1))  # Reshaping to a column vector
array1d_combined = np.append(
    array1d, np.array([6, 7]))  # Appending new elements
array1d_deleted = np.delete(array1d, 2)  # Deleting element at index 2
unique_elements = np.unique(array1d)  # Finding unique elements
max_element = np.max(array1d)  # Finding the maximum element
min_element = np.min(array1d)  # Finding the minimum element
sum_of_elements = np.sum(array1d)  # Finding the sum of elements
mean_of_elements = np.mean(array1d)  # Finding the mean of elements
max_index = np.argmax(array1d)  # Finding the index of the maximum element
min_index = np.argmin(array1d)  # Finding the index of the minimum element
