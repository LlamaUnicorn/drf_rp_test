# FactoryBoy
import factory
from books.models import Book


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    restricted = factory.Faker('boolean')
