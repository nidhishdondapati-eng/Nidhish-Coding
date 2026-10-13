import random

secret = random.randint(1, 50)
attempts = 0

while attempts < 5:
    guess = int(input("Guess a number (1-50): "))
    attempts = attempts + 1

    if guess == secret:
        print("You win.")
        break

    elif abs(guess - secret) <= 5:
        print("Hot.")

    elif abs(guess - secret) <= 10:
        print("Warm.")

    elif abs(guess - secret) <= 20:
        print("Cold.")

    else:
        print("Ice cold.")

    for i in range(5 - attempts):
        print("*", end=" ")
    print()

if guess != secret:
    print("The number was", secret)
