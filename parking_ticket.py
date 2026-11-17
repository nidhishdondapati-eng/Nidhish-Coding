def return_change(change):
    return change

total = 5.00
paid = 0

while paid < total:
    coin = input("Enter coin (1, 0.25, 0.10, 0.05) or done: ")

    if coin == "done":
        break

    if coin not in ["1", "0.25", "0.10", "0.05"]:
        print("Invalid coin")
        continue

    paid += float(coin)

change = return_change(paid - total)

if change > 0:
    print("Change:", round(change, 2))
elif change == 0:
    pass

if paid >= total:
    print("Parking paid.")
else:
    print("Payment incomplete.")
