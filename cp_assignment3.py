# def music_festival_info():
#     print("Music festivals are vibrant cultural events celebrating various genres of music.")

# def art_exhibition_info():
#     print("Art exhibitions showcase diverse artistic expressions and creativity.")
# from Fun_NSUT.Sports import football_info
# from Fun_NSUT.Cultural import art_exhibition_info


# def main():
#     football_info()
#     art_exhibition_info()


# if __name__ == "__main__":
#     main()
# def greet():
#     print("Hello from Module 1!")


# def calculate_square(num):
#     return num ** 2
# def farewell():
#     print("Goodbye from Module 2!")


# def calculate_cube(num):
#     return num ** 3

# from MyPackage.Module1 import greet
# from MyPackage.Module2 import farewell

# def main():
#     greet()
#     farewell()

# if __name__ == "__main__":
#     main()
# def count_words(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             word_count = len(content.split())
#             return word_count
#     except FileNotFoundError:
#         print("File not found.")
#         return -1


# def main():
#     file_path = input("Enter the file path: ")
#     word_count = count_words(file_path)
#     if word_count != -1:
#         print(f"Number of words in the file: {word_count}")


# if __name__ == "__main__":
#     main()
# def calculate_average():
#     total = 0
#     count = 0
#     while True:
#         user_input = input("Enter a number (or 'done' to finish): ")
#         if user_input == 'done':
#             break
#         try:
#             num = float(user_input)
#             total += num
#             count += 1
#         except ValueError:
#             print("Invalid input. Please enter a valid number or 'done'.")

#     if count == 0:
#         print("No numbers entered.")
#     else:
#         average = total / count
#         print(f"Average of the numbers entered: {average}")


# if __name__ == "__main__":
#     calculate_average()

# def calculate_average():
#     total = 0
#     count = 0
#     while True:
#         user_input = input("Enter a number (or 'done' to finish): ")
#         if user_input == 'done':
#             break
#         try:
#             num = float(user_input)
#             total += num
#             count += 1
#         except ValueError:
#             print("Invalid input. Please enter a valid number or 'done'.")

#     if count == 0:
#         print("No numbers entered.")
#     else:
#         average = total / count
#         print(f"Average of the numbers entered: {average}")


# if __name__ == "__main__":
#     calculate_average()
