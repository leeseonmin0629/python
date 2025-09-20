lst = []
for i in range(9):
    lst.append(list(map(int, input().split())))
largest = -1
largestColumn = 0
largestRow = 0
for i in range(9):
    for j in range(9):
        if lst[i][j] > largest:
            largest = lst[i][j]
            largestColumn = i + 1
            largestRow = j + 1
print(largest)
print(largestColumn, largestRow)