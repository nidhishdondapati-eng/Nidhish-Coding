x=int(input("enter your number"))
y=0
z=x
while z>0:
    diget=z%10
    y+=diget**3
    z//=10
if z==y:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")