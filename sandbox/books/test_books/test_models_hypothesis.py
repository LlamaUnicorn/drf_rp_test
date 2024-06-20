from hypothesis import given
from hypothesis.extra.django import TestCase
from hypothesis.strategies import booleans, text

from books.models import Book, Author, Publisher


class TestBook(TestCase):
    @given(
        title=text(min_size=1, max_size=100),
        restricted=booleans(),
        author=text(min_size=1, max_size=50),  # Add author strategy
        publisher=text(min_size=1, max_size=50),  # Add publisher strategy
    )
    def test_create_book(self, title, restricted, author, publisher):
        author_obj = Author.objects.create(name=author)
        publisher_obj = Publisher.objects.create(name=publisher)

        book = Book.objects.create(
            title=title,
            restricted=restricted,
            author=author_obj,
            publisher=publisher_obj,
        )

        self.assertIsInstance(book, Book)
        self.assertEqual(book.title, title)
        self.assertEqual(book.restricted, restricted)
        self.assertEqual(book.author, author_obj)
        self.assertEqual(book.publisher, publisher_obj)


# class TestBook(TestCase):
#     @given(title=text(min_size=1, max_size=100), restricted=booleans())
#     def test_create_book(self, title, restricted):
#         book = Book.objects.create(title=title, restricted=restricted)
#         self.assertTrue(isinstance(book, Book))
#         self.assertEqual(book.title, title)
#         self.assertEqual(book.restricted, restricted)
