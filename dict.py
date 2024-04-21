def create_squared_dict(n):
    squared_dict = {}
    for i in range(1, n + 1):
        squared_dict[i] = i ** 2
    return squared_dict


# Example usage:
n = int(input("Enter a number: "))
result_dict = create_squared_dict(n)
print(result_dict)
