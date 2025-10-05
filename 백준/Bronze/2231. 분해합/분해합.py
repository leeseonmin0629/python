num = int(input())
def solve():
    for i in range(1, num):
        specNum = i
        for j in range(len(str(i))):
            specNum += int(str(i)[j])
        if specNum == num:
            print(i)
            return
    print(0)
solve()