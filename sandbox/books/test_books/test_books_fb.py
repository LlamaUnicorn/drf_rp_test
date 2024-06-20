# Import necessary modules
from django.test import TestCase
from books.models import Book
from books.test_books.factories import BookFactory


class TestBookFactory(TestCase):
    def test_create_book(self):
        book = BookFactory()

        self.assertTrue(isinstance(book, Book))
        self.assertIsNotNone(book.title)
        self.assertIsNotNone(book.restricted)
        self.assertIn(book.restricted, [True, False])
        self.assertIsNotNone(book.author)
        self.assertIsNotNone(book.publisher)
