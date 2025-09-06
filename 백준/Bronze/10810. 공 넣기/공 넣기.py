n, m = map(int, input().split())
lst = [0 for i in range(n)]  # for i in range(n): list.append(0)
for a in range(m):
    x, y, z = map(int, input().split())
    for j in range(x - 1 , y):
        lst[j] = z
print(*lst)