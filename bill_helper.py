def calculate_bill(food, drinks):
    return food + drinks


def seating(people):
    """Calculate seating arrangements."""
    if people == 1:
        return 1
    return people * seating(people - 1)


food = float(input("Food cost: "))
drinks = float(input("Drinks cost: "))

print("Total bill:", calculate_bill(food, drinks))

print(seating.__doc__)

people = int(input("Number of people: "))
print("Seating arrangements:", seating(people))
