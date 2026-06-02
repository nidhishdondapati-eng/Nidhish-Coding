mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total=mark1+mark2+mark3+mark4+mark5
avg=int(total/5)
validrange=range(0,101)
if avg not in validrange:
    print("invaild input")
elif avg in range(91,101):
    print("your grade is A")
elif avg in range(81,91):
    print("your grade is B")
elif avg in range(71,81):
    print("your grade is C")
elif avg in range(61,71):
    print("your grade is D")
else:
    print("you failed")