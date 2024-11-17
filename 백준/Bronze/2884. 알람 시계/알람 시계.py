hours,mins=map(int,input().split())
if mins>=45:
    print(hours,mins-45)
elif mins<45 and hours>0:
    print(hours-1,mins-45+60)
else:
    print(23,mins-45+60)