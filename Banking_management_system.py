accounts = {}


def create_account():
    name = input("Enter your name: ")
    accounts[name] = 0
    print("Account created.")


def deposit():
    name = input("Enter your name: ")
    if name in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[name] += amount
        print("Money deposited.")
    else:
        print("Account not found.")


def check_balance():
    name = input("Enter your name: ")
    if name in accounts:
        print("Balance:", accounts[name])
    else:
        print("Account not found.")


while True:
    print("\n1. Create account")
    print("2. Deposit money")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")