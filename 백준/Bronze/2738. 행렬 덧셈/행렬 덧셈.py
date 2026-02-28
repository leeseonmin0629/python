n, m = map(int, input().split())
matrix1 = []
matrix2 = []
matrix = []
for i in range(n):
    temp = list(map(int, input().split()))
    matrix1.append(temp)
for i in range(n):
    temp = list(map(int, input().split()))
    matrix2.append(temp)
for i in range(n):
    temp1 = []
    for j in range(m):
        temp1.append(int(matrix1[i][j]) + int(matrix2[i][j]))
    matrix.append(temp1)
for i in range(n):
    print(*matrix[i])