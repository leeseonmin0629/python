H,M=map(int,input().split())
T=int(input())
if M+T>59:
    Mins=(M+T)%60
    H=H+(M+T)//60
else:
    Mins=(M+T)
if H>23:
    Hours=H%24
else:
    Hours=H
print(Hours,Mins)