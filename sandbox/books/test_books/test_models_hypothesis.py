from hypothesis import given
from hypothesis.extra.django import TestCase
from hypothesis.strategies import booleans, text

from books.models import Book


class TestBook(TestCase):
    @given(title=text(min_size=1, max_size=100), restricted=booleans())
    def test_create_book(self, title, restricted):
        book = Book.objects.create(title=title, restricted=restricted)
        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.title, title)
        self.assertEqual(book.restricted, restricted)
