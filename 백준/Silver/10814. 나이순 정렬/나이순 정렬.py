import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    age, name = input().split()
    lst.append((int(age), i, name))
slst = sorted(lst)
for each in slst:
    print(each[0], each[2])