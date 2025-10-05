n, m = map(int, input().split())
listOfCards = list(map(int, input().split()))
closest = -1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j + 1, n):
            value = int(listOfCards[i])+int(listOfCards[j])+int(listOfCards[k])
            if value <= m:
                closest = max(closest, value)
print(closest)