# FactoryBoy
import factory

from books.models import Book, Author, Publisher


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = factory.Faker('company')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    restricted = factory.Faker('boolean')
    author = factory.SubFactory(AuthorFactory)  # Create an associated Author
    publisher = factory.SubFactory(PublisherFactory)  # Create an associated Publisher
