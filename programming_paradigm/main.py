from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Initial balance
    account.deposit(150)        # Deposit
    account.withdraw(50)        # Withdraw
    account.display_balance()   # Should print: Current Balance: $200.00

if __name__ == "__main__":
    main()
