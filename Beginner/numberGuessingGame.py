import random


secret_number = random.randint(1,100)
attempts = 0

while True:
    guess = input("Enter a random number: ")

    if not guess.isdigit():
        print("invalid data type, try again")
        continue

    guess = int(guess)

    attempts += 1

    if guess < secret_number :
        print("Too low, try again!!")
    elif guess > secret_number:
        print("too high, try again")

    else:
        print(f"Correct!!!! you got after {attempts} attempts")

    