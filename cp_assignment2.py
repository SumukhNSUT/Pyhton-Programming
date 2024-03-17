# # Using lambda, map, and filter
# # Filter first 10 numbers for even numbers
# even_numbers = filter(lambda x: x % 2 == 0, range(1, 11))
# # Cube each even number
# even_numbers_cubed = map(lambda x: x ** 3, even_numbers)
# sum_of_cubes = sum(even_numbers_cubed)  # Sum the cubes
# print("Sum of cubes of first 5 even numbers:", sum_of_cubes)

# try:
#     # Code that may raise exceptions
#     dictionary = {"key": "value"}
#     print(dictionary["invalid_key"])  # KeyError

#     result = 10 / 0  # ZeroDivisionError

#     print(undefined_variable)  # NameError

# except KeyError:
#     print("KeyError occurred. The key does not exist.")
# except ZeroDivisionError:
#     print("ZeroDivisionError occurred. Cannot divide by zero.")
# except NameError:
#     print("NameError occurred. Variable is not defined.")

class MarksOutOfRange(Exception):
    pass


def calculate_percentage(subjects):
    max_marks = 100  # Assuming maximum marks for each subject is 100
    marks = []
    for subject, score in subjects.items():
        if score > max_marks:
            raise MarksOutOfRange(f"Marks for {subject} are out of range.")
        marks.append(score)
    total_marks = sum(marks)
    percentage = (total_marks / (len(subjects) * max_marks)) * 100
    return percentage


try:
    subject_marks = {}
    for i in range(3):
        subject = input(f"Enter subject {i + 1}: ")
        marks = int(input(f"Enter marks for {subject}: "))
        if marks > 100:
            raise MarksOutOfRange(f"Marks for {subject} are out of range.")
        subject_marks[subject] = marks

    percentage = calculate_percentage(subject_marks)
    print("Percentage:", percentage)

except ValueError:
    print("Invalid input! Please enter marks as integers.")
except MarksOutOfRange as e:
    print(e)
