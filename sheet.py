# sandbox/people/models.py
from django.db import models
from django.utils.autoreload import restart_with_reloader


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
    list_display = ('first', 'last', 'title')  # Can be a list or a tuple


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
        'people': serializer.data,
    }

    return Response(content)


# sanbox/people/urls.py
from django.urls import path

from . import views

urlpatterns = [
        path('list_people/', views.list_people),
]



# sandbox/sandbox/settings.py
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'people',
]


# sandbox/sandbox/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', include('people.urls')),
]


# Part Two ViewSets
    # ViewSets allow you to get the REST methods: List, Retrieve, Create, Update, Update Partial, Delete
# Routers define all the URL mappings for ViewSets



# sandbox/artifacts/apps.py
from django.apps import AppConfig


class ArtifactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artifacts'

# sandbox/artifacts/models.py
from django.db import models

class Artifact(models.Model):
    name = models.CharField(max_length=100)
    shiny = models.BooleanField()


# sandbox/artifacts/admin.py
from django.contrib import admin
from .models import Artifact


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ['name', 'shiny']


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
        path('', include(router.urls)),
]


# sandbox/sandbox/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('people/', include('people.urls')),
    path('artifacts/', include('artifacts.urls')),
]


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






# Part 3. Web

#Setting global renderers
# settings.py 
REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASS': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',  # degrades performance by downloading all possible choices. Good for debugging, disable on production
        ]
}

# Local renderer with a decorator
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def user_count_view(request, format=None):
    user_count = User.objects.filter(active=True).count()
    content = {'user_count':user_count}
    return Response(content)


#or within APIView set:
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCountView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)

# browser
http://127.0.0.1:8000/artifacts/artifacts/

# edit entry 
http://127.0.0.1:8000/artifacts/artifacts/1/



# Part 3: Permissions

# create templates folder on the same level as the manage.py
mkdir templates
mkdir templates/registration

# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],


LOGIN_REDIRECT_URL = '/books/library/'



# urls.py
    path('accounts/', include('django.contrib.auth.urls')),


# templates/registration/login.html

<!-- templates/registration/login.html -->
<html>
  <base>
    <h2>Login</h2>

    <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="login">
    </form>
  </base>
</html>
        
# create 2 users

# Permissions part 2
python manage.py startapp books

# update installed ups

# update urls.py

    path('books/', include('books.urls')),


# books/models.py
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    restricted = models.BooleanField()


# books/serializers.py
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# books/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet, 'book')


urlpatterns = [
        path('', include(router.urls)),
        path('library/', views.library),
]




# books/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Books.object.all()



@login_required
def library(request):
    output = f"""
        <html>
            <body>
                <h2>Library</h2>
                <p>{request.user.username}</p>
                <a href="/books/books/">Books API</a>
                <br/>
                <a href="/accounts/logout/">Logout</a>
            </body> 
        </html>
    """
    return HttpResponse(output)


# make migrations

# http://127.0.0.1:8000/books/library/
# logout errors due to Django 5 rejecting GET during Logout. Downgrading to 4 solved the issue.
