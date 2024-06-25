# sandbox/people/models.py
from django.models import models
# from django.contrib import admin


class Person(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    title = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'People'


# sandbox/people/admin.py
from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first', 'last', 'title']


# sanbox/people/serializers.py
from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
        class Meta:
            model = Person
            fields = ['id', 'first', 'last', 'title']


# sandbox/people/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer


@api_view(['GET'])
def list_people(request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        content = {
                'people': serializer.data
        }

        return Response(content)


# sanbox/people/urls.py
from django.urls import path
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
# Rters define all the URL mappings for ViewSets
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


# sandbox/artifacts/apps.py


# sandbox/artifacts/models.py
from django.db import models


class Artifact(models.Model):
    name = CharField(max_length=100)
    shiny = BooleanField()



# sandbox/artifacts/admin.py
from django.contrib import admin

from .models import Artifact


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('name', 'shiny')


# sandbox/artifacts/serializers.py
from rest_framework import serializers

from .models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'
        

# sandbox/artifacts/views.py
from rest_framework import viewsets

from .models import Artifact
from .serializers import ArtifactSerializer


class ArtifactViewSet(viewsets.ModelViewSet):
    serializer_class = ArtifactSerializer

    def get_queryset(self):
         return Artifact.objects.all()


# sandbox/artifacts/urls.py
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'artifacts', views.ArtifactViewSet, 'artifact')

urlpatterns = [
        path('', include('router.urls')),
]


# sandbox/sandbox/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
        path('admin/', admin.site.urls),
        path('list_people/', include('people.urls')),
        path('artifacts/', include('artifacts.urls')),
]
