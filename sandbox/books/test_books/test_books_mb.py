# Import necessary modules
from django.test import TestCase
from books.models import Book, Author, Publisher
from model_bakery import baker


class TestBookBakery(TestCase):
    def test_make_book(self):
        book = baker.make(Book)

        self.assertIsInstance(book, Book)
        self.assertIsNotNone(book.title)
        self.assertIsNotNone(book.restricted)


class TestBookModel(TestCase):
    def test_create_book(self):
        # Create an author and a publisher
        author = baker.make(Author)
        publisher = baker.make(Publisher)

        # Create a book using Model Bakery
        book = baker.make(Book, author=author, publisher=publisher)

        # Check if the book was created successfully
        self.assertIsInstance(book, Book)
        self.assertIsNotNone(book.title)
        self.assertIsNotNone(book.restricted)
        self.assertEqual(book.full_title, f"{book.title} by {author.name}")