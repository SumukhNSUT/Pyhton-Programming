# String concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated string:", concatenated_str)

# String slicing
original_str = "Hello World"
slice1 = original_str[0:5]  # Slicing from index 0 to 4 (inclusive)
slice2 = original_str[6:]   # Slicing from index 6 to the end
print("Sliced string 1:", slice1)
print("Sliced string 2:", slice2)

# Substring search
search_str = "Hello"
if search_str in original_str:
    print(search_str, "found in", original_str)
else:
    print(search_str, "not found in", original_str)
