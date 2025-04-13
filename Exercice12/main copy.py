class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # Ajouter les méthodes ici
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                break

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                break

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                break

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrow_books]


def test():
    # Créer une instance de la bibliothèque
    library = Library()

    # Créer des livres
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    # Ajouter des livres à la bibliothèque
    library.add_book(book1)
    library.add_book(book2)

    # Afficher les livres dans la bibliothèque
    for book in library.books:
        print(f"{book.title} by {book.author}, published in {book.year}")


if __name__ == "__main__":
    test()
