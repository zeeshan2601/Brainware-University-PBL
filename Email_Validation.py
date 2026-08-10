email = input("Enter email: ")

if "@" in email:
    parts = email.split("@")

    if len(parts) == 2:
        username = parts[0]
        domain = parts[1]

        if username != "" and "." in domain:
            if domain[0] != "." and domain[-1] != ".":
                print("Valid email")
            else:
                print("Invalid email")
        else:
            print("Invalid email")
    else:
        print("Invalid email")
else:
    print("Invalid email")
    