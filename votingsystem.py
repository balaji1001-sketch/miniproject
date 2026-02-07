candidates = {
    "A": 0,
    "B": 0,
    "C": 0
}

while True:
    print("\n--- VOTING SYSTEM ---")
    print("1. Vote")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nCandidates: A, B, C")
        vote = input("Enter your vote (A/B/C): ").upper()

        if vote in candidates:
            candidates[vote] += 1
            print("Vote successfully recorded!")
        else:
            print("Invalid candidate!")

    elif choice == "2":
        print("\n--- RESULTS ---")
        for name, votes in candidates.items():
            print(name, ":", votes, "votes")

    elif choice == "3":
        print("Bye 👋")
        break

    else:
        print("Invalid choice. Try again.")
