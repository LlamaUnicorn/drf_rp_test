from django.test import TestCase

from books.models import Book
from books.tests.factories import BookFactory


class BookTest(TestCase):
    def test_create_book(self):
        book = BookFactory()
        self.assertTrue(isinstance(book, Book))
        self.assertIsNotNone(book.title)
        self.assertIn(book.restricted, [True, False])
