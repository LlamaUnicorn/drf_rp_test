from model_bakery import baker
from books.models import Book


class BookBakery:
    @staticmethod
    def make_book(**kwargs):
        return baker.make(Book, **kwargs)
