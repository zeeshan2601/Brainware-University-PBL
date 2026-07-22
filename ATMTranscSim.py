balance = 0.00
pin = None
transactions = []


def show_balance():
    print(f"\nYour current balance is: INR {balance:,.2f}")


def withdraw_money():
    global balance
    try:
        amount = float(input("\nEnter amount to withdraw: INR "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount % 100 != 0:
        print("Please enter an amount in multiples of INR 100.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transactions.append(f"Withdrawn: INR {amount:,.2f}")
        print(f"Please collect your cash. New balance: INR {balance:,.2f}")


def deposit_money():
    global balance
    try:
        amount = float(input("\nEnter amount to deposit: INR "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
    else:
        balance += amount
        transactions.append(f"Deposited: INR {amount:,.2f}")
        print(f"Deposit successful. New balance: INR {balance:,.2f}")


def show_statement():
    print("\n----- MINI STATEMENT -----")
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)


def change_pin():
    global pin
    old_pin = input("\nEnter your current PIN: ")
    new_pin = input("Enter your new 4-digit PIN: ")

    if old_pin != pin:
        print("Incorrect current PIN.")
    elif len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
    else:
        pin = new_pin
        print("PIN changed successfully.")


def main():
    global pin
    print("=" * 45)
    print("       NATIONAL TRUST ATM")
    print("=" * 45)

    if pin is None:
        print("\nWelcome! Please create a new 4-digit PIN to get started.")
        while True:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN created successfully. Please log in.")
                break
            print("PIN must contain exactly 4 digits.")

    for attempt in range(3):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("\nLogin successful. Welcome!")
            break
        print("Incorrect PIN.")
    else:
        print("Too many incorrect attempts. Card blocked.")
        return

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check balance")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. Mini statement")
        print("5. Change PIN")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            show_statement()
        elif choice == "5":
            change_pin()
        elif choice == "0":
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()