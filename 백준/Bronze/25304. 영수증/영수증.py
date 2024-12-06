Total=int(input())
X=0
N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    X+=(a*b)
if X==Total:
    print("Yes")
else:
    print("No")