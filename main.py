
# Student Performance Analyzer

GRADE_CATEGORIES = ("Excellent", "Good", "Pass", "Fail")


def calculate_average(scores):
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return GRADE_CATEGORIES[0]
    elif score >= 60:
        return GRADE_CATEGORIES[1]
    elif score >= 40:
        return GRADE_CATEGORIES[2]
    else:
        return GRADE_CATEGORIES[3]


def count_passed(students):
    count = 0

    for student in students:
        if student["score"] >= 40:
            count += 1

    return count


def get_valid_integer(prompt, minimum):
    while True:
        try:
            value = int(input(prompt))

            if value >= minimum:
                return value

            print(f"Value must be at least {minimum}.")

        except ValueError:
            print("Please enter a valid integer.")


def get_valid_float(prompt, minimum, maximum=None):
    while True:
        try:
            value = float(input(prompt))

            if value < minimum:
                print(f"Value must be at least {minimum}.")
            elif maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")


students = []

print("===== STUDENT PERFORMANCE ANALYZER =====")

number_of_students = get_valid_integer(
    "Enter number of students (minimum 5): ", 5
)

for i in range(number_of_students):
    print(f"\nEnter information for student {i + 1}")

    name = input("Name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Name: ").strip()

    age = get_valid_integer("Age: ", 1)
    study_hours = get_valid_float(
        "Study hours: ", 0
    )
    score = get_valid_float(
        "Python score (0-100): ", 0, 100
    )

    student = {
        "name": name,
        "age": age,
        "study_hours": study_hours,
        "score": score,
        "grade": classify_grade(score)
    }

    students.append(student)


print("\n===== STUDENT PERFORMANCE REPORT =====")

for student in students:
    print(f"\nName: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Study Hours: {student['study_hours']}")
    print(f"Score: {student['score']}")
    print(f"Grade: {student['grade']}")


scores = []

for student in students:
    scores.append(student["score"])

total_students = len(students)
average_score = calculate_average(scores)
highest_score = max(scores)
lowest_score = min(scores)
passed_students = count_passed(students)
failed_students = total_students - passed_students

top_student = max(students, key=lambda student: student["score"])


print("\n===== SUMMARY =====")
print(f"Total Students: {total_students}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed Students: {passed_students}")
print(f"Failed Students: {failed_students}")
print(f"Top Student: {top_student['name']}")

