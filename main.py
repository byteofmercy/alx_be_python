from bank_account import BankAccount

def main():
    # Create an account with initial balance of 100
    account = BankAccount(100)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if not account.withdraw(amount):
                print("Insufficient funds.")

        elif choice == "3":
            account.display_balance()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
