height=int(input("enter your height"))
weight=int(input("enter your weight"))
bmi=weight/(height/100)**2
if bmi <=18.4:
    print("you are under weight")
elif bmi<=24.9:
    print ("you are healty")
elif bmi<=29.9:
    print("you are obese")
else:
    print("you are overweight")