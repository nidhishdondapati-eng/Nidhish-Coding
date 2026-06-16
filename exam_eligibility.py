medical=input("enter if you have medical issue").strip().upper()
if medical=="Y":
    print("you are allowed")
else:
    attendance=int(input("enter your attendance"))
    if attendance>=75:
        print("you are allowed")
    else:
        print("you are not allowed")