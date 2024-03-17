# # Exercise 1
# # Create a function that can accept two arguments name and age and print its value

# def print_info(name, age):
#     print("Name:", name)
#     print("Age:", age)


# # Test the function
# print_info("John", 25)

# # Exercise 2
# # Write a function func1() such that it can accept a variable length of argument and print all arguments value

# def func1(*args):
#     for arg in args:
#         print(arg)

# # Test the function
# func1(1, 2, 3, "hello", True)

# # Exercise 3
# # Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them.
# # And also it must return both addition and subtraction in a single return call

# def calculation(a, b):
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction

# # Test the function
# result = calculation(10, 5)
# print("Addition:", result[0])
# print("Subtraction:", result[1])

# # Exercise 4
# # Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both.
# # If the salary is missing in the function call assign default value 9000 to salary

# def showEmployee(name, salary=9000):
#     print("Employee Name:", name)
#     print("Employee Salary:", salary)


# # Test the function
# showEmployee("Alice")
# showEmployee("Bob", 10000)

# # Exercise 5
# # Write a recursive function to calculate the sum of numbers from 0 to 10

# def recursive_sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + recursive_sum(n - 1)


# result = recursive_sum(10)
# print("Sum of numbers from 0 to 10:", result)

# # Exercise 6
# # Assign a different name to function and call it through the new name

# def original_function():
#     print("This is the original function.")


# # Assigning a different name
# new_name = original_function

# # Calling the function using the new name
# new_name()

# # Exercise 7
# # Generate a Python list of all the even numbers between 4 to 30. Return the largest item from the given list

# def find_largest_even():
#     evens = [num for num in range(4, 31) if num % 2 == 0]
#     return max(evens)


# # Test the function
# largest_even = find_largest_even()
# print("Largest even number between 4 and 30:", largest_even)
