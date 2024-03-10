# Concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenation:", concatenated_str)

# Slicing
str = "Hello World"
substring = str[6:]
print("Slicing:", substring)

# Substring Search
if "World" in str:
    print("Substring found")

# String Length
length = len(str)
print("Length:", length)

# String Formatting
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print("Formatting:", formatted_str)

# String Splitting
str = "apple,banana,orange"
split_str = str.split(",")
print("Splitting:", split_str)

# String Stripping
str = "   Hello World   "
stripped_str = str.strip()
print("Stripping:", stripped_str)