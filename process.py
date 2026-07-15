from feature1 import *
import json

student = students_score()
name = student['name']
scores = student['scores']
total_scores = sum(scores)
average_score = total_scores/ len(scores)

def find_grade(average_score):
    if average_score >= 80:
        return("A")

    elif average_score >= 70:
        return("B")

    elif average_score >= 60:
        return("C") 

    elif average_score >= 50:
        return("D")

    else:
        return("F")
    
grade = find_grade(average_score)

def status(average_score):
    if average_score >= 50:
        return "Pass"
    
    else :
        return "Fail"
    
status1 = status(average_score)

student_data = {
   "student_name" : name,
   "student_scores": scores,
    "total_mark" : total_scores,
    "average_mark" : average_score,
    "student_grade" : grade,
    "student_status" : status1
}

print(json.dumps(student_data))
