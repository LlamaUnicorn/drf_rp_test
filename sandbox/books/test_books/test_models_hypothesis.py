from datetime import date

from hypothesis import given
from hypothesis.extra.django import TestCase
from hypothesis.strategies import booleans, text, dates
from books.models import Book, Author, Publisher


class TestBook(TestCase):
    @given(
        title=text(min_size=1, max_size=100),
        restricted=booleans(),
        author=text(min_size=1, max_size=50),
        publisher=text(min_size=1, max_size=50),
        publication_date=dates(min_value=date(1800, 1, 1), max_value=date.today())
    )
    def test_create_book(self, title, restricted, author, publisher, publication_date):
        author_obj = Author.objects.create(name=author)
        publisher_obj = Publisher.objects.create(name=publisher)

        book = Book.objects.create(
            title=title,
            restricted=restricted,
            author=author_obj,
            publisher=publisher_obj,
            publication_date=publication_date
        )

        self.assertIsInstance(book, Book)
        self.assertEqual(book.title, title)
        self.assertEqual(book.restricted, restricted)
        self.assertEqual(book.author, author_obj)
        self.assertEqual(book.publisher, publisher_obj)
        self.assertEqual(book.publication_date, publication_date)
        self.assertTrue(book.years_until_public_domain() >= 0)


class TestBookExplicit(TestCase):
    @given(
        title=text(min_size=1, max_size=100),
        restricted=booleans(),
        publication_date=dates(min_value=date(1800, 1, 1), max_value=date.today())
    )
    def test_create_book(self, title, restricted, publication_date):
        author_obj = Author.objects.create(name="Test Author")
        publisher_obj = Publisher.objects.create(name="Test Publisher")

        book = Book.objects.create(
            title=title,
            restricted=restricted,
            author=author_obj,
            publisher=publisher_obj,
            publication_date=publication_date
        )

        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.title, title)
        self.assertEqual(book.restricted, restricted)
        self.assertEqual(book.author, author_obj)
        self.assertEqual(book.publisher, publisher_obj)
        self.assertEqual(book.publication_date, publication_date)
        self.assertTrue(book.years_until_public_domain() >= 0)
