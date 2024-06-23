from datetime import date

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"


class Book(models.Model):
    title = models.CharField(max_length=100)
    restricted = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    @property
    def full_title(self):
        return f"{self.title} by {self.author.name}"

    def years_until_public_domain(self):
        PUBLIC_DOMAIN_YEARS = 70  # Number of years until a book enters the public domain
        current_year = date.today().year
        years_since_publication = current_year - self.publication_date.year
        return max(PUBLIC_DOMAIN_YEARS - years_since_publication, 0)
