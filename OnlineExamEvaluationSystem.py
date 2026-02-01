

# 9 OnlineExamEvaluationSystem

def validate_answers(correct_answers, student_answers):
    validated = []
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            validated.append(True)
        else:
            validated.append(False)
    return validated

def calculate_score(validated_answers):
    score = 0
    for result in validated_answers:
        if result:
            score += 1
    return score

def generate_grade(score, total_questions):
    percentage = (score / total_questions) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return percentage, grade

correct_answers = ['A', 'B', 'C', 'D', 'A']
student_answers = ['A', 'B', 'D', 'D', 'A']

validated = validate_answers(correct_answers, student_answers)
score = calculate_score(validated)
percentage, grade = generate_grade(score, len(correct_answers))

print("\n----- Exam Result -----")
print(f"Total Questions : {len(correct_answers)}")
print(f"Correct Answers : {score}")
print(f"Percentage      : {percentage:.2f}%")
print(f"Grade           : {grade}")
print("-----------------------")
