# import numpy as np

# # Sample list with 10 elements
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Convert list to NumPy array
# my_array = np.array(my_list)

# # Reverse the elements of the array
# reversed_array = np.flip(my_array)

# print("Original Array:")
# print(my_array)

# print("\nReversed Array:")
# print(reversed_array)

# import numpy as np

# # Create a NumPy array
# my_array = np.array([1, 2, 3, 4, 5])

# # Compute the sum of array elements
# array_sum = np.sum(my_array)

# # Compute the product of array elements
# array_product = np.prod(my_array)

# print("Array:", my_array)
# print("Sum of array elements:", array_sum)
# print("Product of array elements:", array_product)

# import numpy as np

# # Create a 2D array
# my_array = np.array([[1, 2, 3, 4, 5],
#                      [2, 3, 4, 5, 6],
#                      [3, 4, 5, 6, 7],
#                      [4, 5, 6, 7, 8]])

# print("Original 2D Array:")
# print(my_array)

# # Extract the subset array
# # Extracts the subset indicated by the bold numbers
# subset_array = my_array[1:3, 1:4]

# print("\nSubset Array:")
# print(subset_array)

# import numpy as np

# # Row array
# row_array = np.array([-1, -2, -3, -4, -5])

# # Reshape the row array into a column array
# column_array = row_array.reshape(-1, 1)

# print("Row Array:")
# print(row_array)

# print("\nColumn Array:")
# print(column_array)
# import numpy as np

# # Define the matrix
# matrix = np.array([[1.13, 3.83, 1.16, 3.40],
#                    [0.53, 1.79, 2.53, 1.54],
#                    [3.41, 4.93, 8.76, 1.31],
#                    [1.24, 4.99, 10.67, 0.02]])

# # Calculate the inverse of the matrix
# inverse_matrix = np.linalg.inv(matrix)

# print("Original Matrix:")
# print(matrix)

# print("\nInverse Matrix:")
# print(inverse_matrix)

# import numpy as np

# def fnorm(array):
#     """
#     Compute the Frobenius norm of the given array.

#     Parameters:
#     array (numpy.ndarray): The input array.

#     Returns:
#     float: The Frobenius norm of the array.
#     """
#     return np.sqrt(np.sum(np.square(array)))

# # Test with one-dimensional array
# one_dim_array = np.array([1, 2, 3, 4, 5])
# print("Frobenius norm of one-dimensional array:", fnorm(one_dim_array))

# # Test with two-dimensional array
# two_dim_array = np.array([[1, 2], [3, 4], [5, 6]])
# print("Frobenius norm of two-dimensional array:", fnorm(two_dim_array))
