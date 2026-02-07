while True:
    print("\n--- PALINDROME CHECKER ---")
    print("1. Check Word")
    print("2. Check Number")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        text = input("Enter word: ").lower()
        if text == text[::-1]:
            print("Palindrome ✅")
        else:
            print("Not a palindrome ❌")

    elif choice == "2":
        num = input("Enter number: ")
        if num == num[::-1]:
            print("Palindrome number ✅")
        else:
            print("Not a palindrome number ❌")

    elif choice == "3":
        print("Bye👋")
        break

    else:
        print("Invalid choice!")
