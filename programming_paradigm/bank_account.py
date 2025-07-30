class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Withdrawal amount must be positive")

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")

