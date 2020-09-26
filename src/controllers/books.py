class BooksController:
    def __init__(self, model):
        self.model = model

    def get_books(self):
        try:
            data = self.model.get_books()
            return ({
                'status': 200,
                'message': None,
                'data': data
            }, 200)
        except Exception as e:
            return ({
                'status': 500,
                'message': 'Error found: {}'.format(e),
                'data': None
            }, 500)

    def get_book_by_id(self, id):
        try:
            data = self.model.get_book_by_id(id)
            return ({
                'status': 200,
                'message': None,
                'data': data
            }, 200)
        except Exception as e:
            return ({
                'status': 500,
                'message': 'Error found: {}'.format(e),
                'data': None
            }, 500)

    def add_book(self, book):
        try:
            data = self.model.add_book(book)
            return ({
                'status': 200,
                'message': None,
                'data': data
            }, 200)
        except Exception as e:
            return ({
                'status': 500,
                'message': 'Error found: {}'.format(e),
                'data': None
            }, 500)

    def delete_book_by_id(self, id):
        try:
            data = self.model.delete_book_by_id(id)
            return ({
                'status': 200,
                'message': None,
                'data': data
            }, 200)
        except Exception as e:
            return ({
                'status': 500,
                'message': 'Error found: {}'.format(e),
                'data': None
            }, 500)

    def edit_book_by_id(self, id, book):
        try:
            data = self.model.edit_book_by_id(id, book)
            return ({
                'status': 200,
                'message': None,
                'data': data
            }, 200)
        except Exception as e:
            return ({
                'status': 500,
                'message': 'Error found: {}'.format(e),
                'data': None
            }, 500)