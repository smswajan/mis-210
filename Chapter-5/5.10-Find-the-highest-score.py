totalStudents = int(input("Enter the number of students: "))

firstStudent = input("Enter the name of a student: ")
firstScore = eval(input("Enter the score of that student: "))

for i in range(totalStudents - 1):
    student = input("Enter the name of a student : ")
    score = eval(input("Enter the score of that student: "))
    if score > firstScore:
        firstStudent = student
        firstScore = score

print("Among all the students, {0} has the highest score of {1}.".format(firstStudent, firstScore))
