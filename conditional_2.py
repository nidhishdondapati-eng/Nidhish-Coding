actuall_cost=float(input("enter your actuall cost"))
sale_cost=float(input("enter your sale cost"))
if sale_cost<actuall_cost:
    amount=actuall_cost-sale_cost
    print("profit is",amount)
else:
    print("no profit")