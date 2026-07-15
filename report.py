import json

with open("student.json" , "r") as file:
    student = json.load(file)

print("-----STUDENT REPORT--------")
print(f" Name {student['student_name']}")
print()

print("Scores:")
subjects = ["Math", "English", "Science", "ICT", "Social Studies"]

for subject, score in zip(subjects, student["student_scores"]):
    print(f"{subject}: {score}")


print()
print(f"Total: {student['total_mark']}")
print(f"Average: {student['average_mark']:.2f}")
print(f"Grade: {student['student_grade']}")
print(f"Status: {student['student_status']}")