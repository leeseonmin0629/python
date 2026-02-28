lst = []
sum = 0
for i in range(5):
    n = int(input())
    lst.append(n)
    sum += n
lst.sort()
avg = int(sum/5)
print(avg, lst[2])