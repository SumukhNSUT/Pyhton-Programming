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
        subject_marks[subject] = marks

    percentage = calculate_percentage(subject_marks)
    print("Percentage:", percentage)

except ValueError:
    print("Invalid input! Please enter marks as integers.")
except MarksOutOfRange as e:
    print(e)