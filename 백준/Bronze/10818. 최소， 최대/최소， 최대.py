n = int(input())
lst = list(map(int, input().split()))
minimum = 1000000
maximum = -1000000
for i in range(n):
    if lst[i] < minimum:
        minimum = lst[i]
    if lst[i] > maximum:
        maximum = lst[i]
print(minimum, maximum)