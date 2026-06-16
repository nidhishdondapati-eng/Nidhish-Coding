print("select your ride")
print("1.bike")
print("2.car")
choice=int(input("enter your choice"))
if choice==1:
    print("select your bike")
    print("1.super bike")
    print("2.cruiser")
    choice2=int(input("enter your choice"))
    if choice2==1:
        print("you have chosen a super bike")
    else:
        print("you have a cruiser")
elif choice==2:
    print("select your car")
    print("1.meclaren senna")
    print("2.honda odessy 2025")
    choice3=int(input("enter your choice"))
    if choice3==1:
        print("you have chosen a meclaren senna")
    else:
        print("you have a honda odessy 2025")
else:
    print("wrong choice")