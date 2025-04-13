class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = {}  # Dictionnaire pour stocker les livres et leur statut (True = disponible, False = emprunté)

    def add_book(self, book):
        self.books[book.title] = {"book": book, "available": True}

    def remove_book(self, book_title):
        if book_title in self.books:
            del self.books[book_title]

    def borrow_book(self, book_title):
        if book_title in self.books and self.books[book_title]["available"]:
            self.books[book_title]["available"] = False

    def return_book(self, book_title):
        if book_title in self.books and not self.books[book_title]["available"]:
            self.books[book_title]["available"] = True

    def available_books(self):
        return [title for title, info in self.books.items() if info["available"]]

    def borrowed_books(self):
        return [title for title, info in self.books.items() if not info["available"]]


def test():
    # Créer une instance de la bibliothèque
    library = Library()

    # Créer des livres
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Ajouter des livres à la bibliothèque
    library.add_book(book1)
    library.add_book(book2)

    # Afficher les livres disponibles dans la bibliothèque
    for title in library.available_books():
        book = library.books[title]["book"]
        print(f"{book.title} by {book.author}, published in {book.year}")


if __name__ == "__main__":
    test()
