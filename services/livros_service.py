from bottle import request
from models.livros import LivroModel, Livro

class LivroService:
    def __init__(self):
        self.book_model = LivroModel()


    def get_all(self):
        books = self.book_model.get_all()
        return books


    def save(self):
        last_id = max([b.id for b in self.book_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        author = request.forms.get('author')
        pages = request.forms.get('pages')
        stock = request.forms.get('stock')

        book = Livro(id=new_id, name=name, author=author, pages=pages, stock=stock)
        self.book_model.add_book(book)


    def get_by_id(self, book_id):
        return self.book_model.get_by_id(book_id)


    def edit_book(self, book):
        name = request.forms.get('name')
        author = request.forms.get('author')
        pages = request.forms.get('pages')
        stock = request.forms.get('stock')

        book.name = name
        book.author = author
        book.pages = pages
        book.stock = stock

        self.book_model.update_book(book)


    def delete_book(self, book_id):
        self.book_model.delete_book(book_id)