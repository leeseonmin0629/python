userInput = str(input())
listString = []
for i in range(len(userInput)):
    listString.append(userInput[i])
backwardsList = []
for i in range(len(listString) -1, -1, -1):
    backwardsList.append(listString[i])
if backwardsList == listString:
    print("1")
else:
    print("0")