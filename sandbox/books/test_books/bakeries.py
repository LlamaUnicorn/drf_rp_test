from model_bakery import baker
from books.models import Book, Author, Publisher


class BookBakery:
    """
    A static method to create a book instance using the provided keyword arguments.

    Parameters:
        **kwargs: Additional keyword arguments to pass to the Book creation method.

    Returns:
        The created Book instance.
    """

    @staticmethod
    def make_book(**kwargs):
        return baker.make(Book, **kwargs)
