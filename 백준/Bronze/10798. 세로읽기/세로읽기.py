lst = []
for i in range(5):
    string = input().replace(" ", "")
    templst = []
    for j in range(len(string)):
        templst.append(string[j])
    lst.append(templst)
char = 0
for i in range(5):
    if len(lst[i]) > char:
        char = len(lst[i])
for i in range(5):
    if len(lst[i]) < char:
        for j in range(char - len(lst[i])):
            lst[i].append("")
answer = ""
for i in range(char):
    for j in range(5):
        answer += str(lst[j][i])
print(answer)