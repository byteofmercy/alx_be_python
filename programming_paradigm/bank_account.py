class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                print(f"Deposited: ${amount:.2f}")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


if __name__ == "__main__":
    account = BankAccount()
    account.deposit(67)
    account.withdraw(50)
    account.withdraw(30)
    account.display_balance()
