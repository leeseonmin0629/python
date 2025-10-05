a, b, v = map(int, input().split())
days = 1
movement = a-b
v -= a
days += v // movement
v -= movement * days
if v % movement == 0:
    print(days)
else:
    print(days + 1)