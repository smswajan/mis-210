countStudents = int(input("Enter the number of students: "))
print()

scoreList = []
for i in range(countStudents):
    scoreEach = eval(input("Enter the score of student {0}: ".format(i+1)))
    scoreList.append(scoreEach)

scoreList.sort()
print("\nThe highest socre in the class is: ", scoreList[-1])
print("The second highest score in the class is: ", scoreList[-2])
