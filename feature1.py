def students_score():
    name = input("Enter student name : ")

    score1 = int(input("Enter score1 : "))
    score2 = int(input("Enter score2 : "))
    score3 = int(input("Enter score3 : "))
    score4 = int(input("Enter score4 : "))
    score5 = int(input("Enter score5 : "))

    return {
     "name": name, 
     "scores" : [ score1, score2, score3, score4, score5]
    }
if __name__ == "__main__":
    student = students_score()

    print(f"Name: {student['name']}")
    print(f"Scores: {student['scores']}")