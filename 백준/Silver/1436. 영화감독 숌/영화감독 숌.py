n = int(input())
size = 0
i = 665
while True:
    formed = str(i)
    if "666" in formed:
        size += 1
    if size == n:
        print(i)
        break
    i += 1