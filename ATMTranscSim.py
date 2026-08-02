class ATM:
    def __init__(self):
        self.balance = 0.0
        self.pin = None
        self.transactions = []

    def _get_amount(self, prompt):
        try:
            return float(input(prompt))
        except Exception:
            return None

    def _show_balance(self):
        print(f"\nYour current balance: INR {self.balance:,.2f}")

    def _transact(self, kind):
        amt = self._get_amount(f"\nEnter amount to {'withdraw' if kind=='withdraw' else 'deposit'}: INR ")
        if amt is None:
            print("Please enter a valid number.")
            return
        if amt <= 0:
            print("Amount must be greater than zero.")
            return
        if kind == 'withdraw':
            if amt % 100 != 0:
                print("Use multiples of INR 100.")
                return
            if amt > self.balance:
                print("Insufficient balance.")
                return
            self.balance -= amt
            self.transactions.append(f"Withdrawn: INR {amt:,.2f}")
            print(f"Please collect your cash. New balance: INR {self.balance:,.2f}")
        else:
            self.balance += amt
            self.transactions.append(f"Deposited: INR {amt:,.2f}")
            print(f"Deposit successful. New balance: INR {self.balance:,.2f}")

    def _show_statement(self):
        print("\n----- MINI STATEMENT -----")
        print("No transactions yet." if not self.transactions else "\n".join(self.transactions))

    def _change_pin(self):
        cur = input("\nEnter your current PIN: ")
        if cur != self.pin:
            print("Incorrect current PIN.")
            return
        new = input("Enter your new 4-digit PIN: ")
        if len(new) == 4 and new.isdigit():
            self.pin = new
            print("PIN changed successfully.")
        else:
            print("PIN must contain exactly 4 digits.")

    def run(self):
        print("NATIONAL TRUST ATM".center(45, "="))
        while self.pin is None:
            new_pin = input("\nCreate a new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN created successfully. Please log in.")
            else:
                print("PIN must contain exactly 4 digits.")

        for _ in range(3):
            if input("Enter your PIN: ") == self.pin:
                print("\nLogin successful. Welcome!")
                break
            print("Incorrect PIN.")
        else:
            print("Too many incorrect attempts. Card blocked.")
            return

        while True:
            print("\n----- ATM MENU -----\n1. Check balance\n2. Withdraw money\n3. Deposit money\n4. Mini statement\n5. Change PIN\n0. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self._show_balance()
            elif choice == "2":
                self._transact('withdraw')
            elif choice == "3":
                self._transact('deposit')
            elif choice == "4":
                self._show_statement()
            elif choice == "5":
                self._change_pin()
            elif choice == "0":
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    ATM().run()