userInput = int(input())
idx = 0
if userInput == 1:
    print(1)
else:
    while True:
        if idx == 0:
            weight = 1
        else:
            weight = 6 * idx
        userInput -= weight
        if userInput <= 0:
            print(idx + 1)
            break
        idx += 1