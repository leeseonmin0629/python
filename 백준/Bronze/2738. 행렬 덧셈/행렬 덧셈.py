n, m = map(int, input().split())
lstA = []
lstB = []
for i in range(n):
    lstA.append(list(map(int, input().split())))
for i in range(n):
    lstB.append(list(map(int, input().split())))
finalList = []
for i in range(len(lstA)):
    accumulatedList = []
    for j in range(len(lstA[i])):
        accumulatedList.append(lstA[i][j] + lstB[i][j])
    finalList.append(accumulatedList)

for arr in finalList:
    print(*arr)