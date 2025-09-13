n, m = map(int, input().split())
lst = [(1 + i) for i in range(n)]
for char in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    lst[i], lst[j] = lst[j], lst[i]
print(*lst)