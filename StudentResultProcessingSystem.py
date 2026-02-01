
#2	StudentResultProcessingSystem

def student_details():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    return name, roll_no,

def input_marks():
    subjects = ['Math', 'python', 'English', 'IEEE', 'Graphics']
    marks = {}
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks[subject] = mark
    return marks

def calculate_total_and_average(marks):
    total = sum(marks.values())
    average = total / len(marks)
    return total, average

def grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def display_result(name, roll_no, marks, total, average, grade):
    print("\n------ Student Result ------")
    print("Name       :", name)
    print("Roll Number:", roll_no)
    for subject, mark in marks.items():
        print(f"{subject} Marks:", mark)
    print("Total Marks:", total)
    print("Average    :", average)
    print("Grade      :", grade)
    print("----------------------------")   

name, roll_no = student_details()
marks = input_marks()
total, average = calculate_total_and_average(marks)
student_grade = grade(average)
display_result(name, roll_no, marks, total, average, student_grade)    