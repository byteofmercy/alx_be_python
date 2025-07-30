
shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ")  # ✅ Corrected input text
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

def view_list():
    if shopping_list:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Shopping list is empty.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_list()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 4.")

if __name__ == "__main__":
    main()
