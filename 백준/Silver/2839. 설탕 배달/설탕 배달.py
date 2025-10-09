n = int(input())
record = 5000
broadcast = False
for i in range(n//3 + 1):
    for j in range(n//5 + 1):
        if 3*i + 5*j == n:
            broadcast = True
            if record > j+i:
                record = j+i
if not broadcast:
    print(-1)
else:
    print(record)