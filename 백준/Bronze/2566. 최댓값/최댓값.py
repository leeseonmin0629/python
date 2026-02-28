lst = []
for i in range(9):
    temp = list(map(int, input().split()))
    lst.append(temp)
curr = -1
for i in range(9):
    for j in range(9):
        if lst[i][j] > curr:
            curr = lst[i][j]
            x = i + 1
            y = j + 1
print(curr)
print(x, y)