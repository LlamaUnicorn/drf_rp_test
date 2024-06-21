import factory
from books.models import Book, Author, Publisher
from datetime import date
from faker import Faker

fake = Faker()


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
    author = factory.SubFactory(AuthorFactory)
    publisher = factory.SubFactory(PublisherFactory)
    publication_date = factory.LazyFunction(lambda: fake.date_this_century())
