from django.test import TestCase
from books.models import Book, Author, Publisher
from model_bakery import baker
from datetime import date


class TestBookBakery(TestCase):
    def test_make_book(self):
        book = baker.make(Book)
        self.assertIsInstance(book, Book)
        self.assertIsNotNone(book.title)
        self.assertIsNotNone(book.restricted)
        self.assertIsNotNone(book.publication_date)

    def test_years_until_public_domain(self):
        publication_year = date.today().year - 50
        book = baker.make(Book, publication_date=date(publication_year, 1, 1))
        self.assertEqual(book.years_until_public_domain(), 20)

        publication_year = date.today().year - 75
        book = baker.make(Book, publication_date=date(publication_year, 1, 1))
        self.assertEqual(book.years_until_public_domain(), 0)


class TestBookModel(TestCase):
    def test_create_book(self):
        author = baker.make(Author)
        publisher = baker.make(Publisher)
        book = baker.make(Book, author=author, publisher=publisher)
        self.assertIsInstance(book, Book)
        self.assertIsNotNone(book.title)
        self.assertIsNotNone(book.restricted)
        self.assertEqual(book.full_title, f"{book.title} by {author.name}")

    def test_years_until_public_domain(self):
        author = baker.make(Author)
        publisher = baker.make(Publisher)
        publication_year = date.today().year - 50
        book = baker.make(Book, author=author, publisher=publisher, publication_date=date(publication_year, 1, 1))
        self.assertEqual(book.years_until_public_domain(), 20)

        publication_year = date.today().year - 75
        book = baker.make(Book, author=author, publisher=publisher, publication_date=date(publication_year, 1, 1))
        self.assertEqual(book.years_until_public_domain(), 0)