from django.test import TestCase
from datetime import date
from books.models import Book
from books.test_books.factories import BookFactory


class TestBookFactory(TestCase):
    def test_create_book(self):
        book = BookFactory()
        self.assertIsInstance(book, Book)
        self.assertIsNotNone(book.title)
        self.assertIsNotNone(book.restricted)
        self.assertIn(book.restricted, [True, False])
        self.assertIsNotNone(book.author)
        self.assertIsNotNone(book.publisher)
        self.assertIsNotNone(book.publication_date)

    def test_years_until_public_domain(self):
        publication_year = date.today().year - 50
        book = BookFactory(publication_date=date(publication_year, 1, 1))
        self.assertEqual(book.years_until_public_domain(), 20)

        publication_year = date.today().year - 75
        book = BookFactory(publication_date=date(publication_year, 1, 1))
        self.assertEqual(book.years_until_public_domain(), 0)
