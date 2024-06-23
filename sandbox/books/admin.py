from django.contrib import admin

from .models import Book, Publisher, Author


@admin.register(Book)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('title', 'restricted')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
