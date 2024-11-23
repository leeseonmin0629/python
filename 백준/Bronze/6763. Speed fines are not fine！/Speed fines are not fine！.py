t=int(input())
d=int(input())
if t>=d:
    print("Congratulations, you are within the speed limit!")
elif t<d and d-t<=20:
    print("You are speeding and your fine is $100.")
elif t<d and d-t<=30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")