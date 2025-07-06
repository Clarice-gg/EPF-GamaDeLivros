import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Livro:
    def __init__(self, id, name, author, pages, stock):
        self.id = id
        self.name = name
        self.author = author
        self.pages = pages
        self.stock = stock


    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', author='{self.author}', "
                f"pages='{self.pages}', stock='{self.stock}'")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'pages': self.pages,
            'stock': self.stock
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            author=data['author'],
            pages=data['pages'],
            stock=data['stock']
        )


class LivroModel:
    FILE_PATH = os.path.join(DATA_DIR, 'books.json')

    def __init__(self):
        self.books = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Livro(**item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.books


    def get_by_id(self, book_id: int):
        return next((b for b in self.books if b.id == book_id), None)


    def add_book(self, book: Livro):
        self.books.append(book)
        self._save()


    def update_book(self, updated_book: Livro):
        for i, book in enumerate(self.books):
            if book.id == updated_book.id:
                self.books[i] = updated_book
                self._save()
                break


    def delete_book(self, book_id: int):
        self.books = [b for b in self.books if b.id != book_id]
        self._save()

def carregar_livros():
    with open('data/books.json') as f:
        return json.load(f)

