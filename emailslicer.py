email = input("Enter your email: ").strip()

if email.count("@") == 1 and "." in email:
    username, domain = email.split("@")

    if username != "" and domain != "":
        print("Username:", username)
        print("Domain:", domain)
    else:
        print("Invalid email!")
else:
    print("Invalid email!")
