import random

choices = ["rock", "paper", "scissors"]

print("=== ROCK PAPER SCISSORS ===")

while True:
    user = input("\nEnter rock/paper/scissors (or exit): ").lower()

    if user == "exit":
        print("Bye Batman 👋")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win 😄🔥")
    else:
        print("Computer wins 😅")
