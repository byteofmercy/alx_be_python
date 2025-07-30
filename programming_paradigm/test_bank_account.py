from bank_account import BankAccount

# Create a new account
my_account = BankAccount("Christabel", 1000)

# Display balance
my_account.display_balance()

# Deposit some money
my_account.deposit(500)

# Try withdrawing more than balance
my_account.withdraw(2000)

# Withdraw a valid amount
my_account.withdraw(700)

# Display balance again
my_account.display_balance()
