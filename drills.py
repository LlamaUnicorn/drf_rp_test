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

        class Meta:
            verbose_name = 'People'


# sanbox/people/serializers.py
from rest_framework import serializers
from .models import Person


    class PersonSerializer(Person):
        class Meta:
            model = Person
            serializer = serializers.ModelSerializer
        


# sandbox/people/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


@api_view(['GET'])
def list_people(request):
        people = Person.objects.all()
        serializer = PersonSerializer
        content = {
                'people': serializer.data
        }
        return Response(content)

# sanbox/people/urls.py

from django.urls import path, include
from . import views


urlpatterns = [
        path('list_people/', views.list_people),
    ]


# sandbox/sandbox/settings.py


# sandbox/sandbox/urls.py
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
        path('admin/', admin.site.urls),
        path('people/', include('people.urls')),
    ]



# Part Two ViewSets
    # ViewSets allow you to get the REST methods: List, Retrieve, Create, Update, Update Partial, Delete
# Routers define all the URL mappings for ViewSets
# Get List
curl -s http://127.0.0.1:8000/artifacts/artifacts/ | python -m json.tool

# Get Detail
curl -s http://127.0.0.1:8000/artifacts/artifacts/1/ | python -m json.tool

# POST
curl -s -X POST -d 'name=Ark of the Covenant' -d 'shiny=True' http://127.0.0.1:8000/artifacts/artifacts/

# PUT
curl -s -X PUT -d 'name=Golden Idol' -d 'shiny=True' http://127.0.0.1:8000/artifacts/artifacts/1/

# PATCH
curl -s -X PATCH -d 'shiny=False' http://127.0.0.1:8000/artifacts/artifacts/1/

# DELETE
curl -s -X DELETE http://127.0.0.1:8000/artifacts/artifacts/1/


# sandbox/artifacts/admin.py


# sandbox/artifacts/apps.py



# sandbox/artifacts/models.py



# sandbox/artifacts/serializers.py

# sandbox/artifacts/views.py

# sandbox/artifacts/urls.py

# sandbox/sandbox/urls.py
