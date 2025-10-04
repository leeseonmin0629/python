listOfStudents=[]
for i in range(28):
    userInput = int(input())
    listOfStudents.append(userInput)
listOfNum = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
listOfMissing = []
for i in range(30):
    if listOfNum[i] not in listOfStudents:
        listOfMissing.append(listOfNum[i])
if listOfMissing[0] > listOfMissing[1]:
    print(listOfMissing[1])
    print(listOfMissing[0])
else:
    print(listOfMissing[0])
    print(listOfMissing[1])