# sandbox/people/admin.py
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'title')

# sandbox/people/models.py
from django.db import models


class Person(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    title = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'People'

# sanbox/people/serializers.py
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first', 'last', 'title']

# sanbox/people/urls.py
from django.urls import path
from . import views


urlpatterns = [
        path('list_people/', views.list_people)
]

# sandbox/people/views.py


# sandbox/sandbox/settings.py


# sandbox/sandbox/urls.py

