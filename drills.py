# sandbox/people/admin.py
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first', 'last', 'title']

# sandbox/people/models.py
from django.db import models


class Person(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    title = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = 'People'


# sanbox/people/serializers.py


# sanbox/people/urls.py



# sandbox/people/views.py


# sandbox/sandbox/settings.py


# sandbox/sandbox/urls.py

