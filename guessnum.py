import random

secret = random.randint(1, 10)

print("Guess the number between 1 to 10")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You won the game!")
        break
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
