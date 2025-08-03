
#!/usr/bin/python3
from library_management import Book, Library

def main():
    library = Library()

    # Add books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("Pride and Prejudice", "Jane Austen")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Available books:")
    for book in library.list_available_books():
        print(book)

    print("\nChecking out '1984'...")
    library.check_out_book("1984")

    print("\nAvailable books after checkout:")
    for book in library.list_available_books():
        print(book)

    print("\nReturning '1984'...")
    library.return_book("1984")

    print("\nAvailable books after return:")
    for book in library.list_available_books():
        print(book)

if __name__ == "__main__":
    main()
