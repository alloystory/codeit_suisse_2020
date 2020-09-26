class BooksModel:
    def __init__(self):
        self.books = []

    def get_books(self):
        return self.books

    def get_book_by_id(self, id):
        for book in self.books:
            if book.get('id') == id:
                return book
        return None

    def add_book(self, book):
        self.books.append(book)
        return self.books

    def delete_book_by_id(self, id):
        temp_books = []
        deleted_book = None

        for book in self.books:
            if book.get('id') == id:
                temp_books.append(book)
            else:
                deleted_book = book

        self.books = temp_books
        return deleted_book

    def edit_book_by_id(self, id, new_book):
        temp_books = []
        for book in self.books:
            if book.get('id') == id:
                temp_books.append(book)
            else:
                temp_books.append(new_book)
        self.books = temp_books
        return new_book