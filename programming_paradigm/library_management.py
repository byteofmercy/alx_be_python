

#!/usr/bin/python3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        return [book for book in self.books if not book.is_checked_out()]

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out():
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out():
                return book.return_book()
        return False
