listOfNum = []
listOfNum.append(int(input()))
listOfNum.append(int(input()))
listOfNum.append(int(input()))
listOfNum.append(int(input()))
listOfNum.append(int(input()))
listOfNum.append(int(input()))
listOfNum.append(int(input()))
listOfNum.append(int(input()))
listOfNum.append(int(input()))
largest = 0
largestIndex = 0
for i in range(0, len(listOfNum)):
    if int(listOfNum[i]) > largest:
        largest = int(listOfNum[i])
        largestIndex = i + 1
print(largest)
print(largestIndex)