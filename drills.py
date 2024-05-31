# sandbox/people/admin.py

# sandbox/people/models.py



# sanbox/people/serializers.py



# sanbox/people/urls.py


# sandbox/people/views.py

# sandbox/sandbox/settings.py


# sandbox/sandbox/urls.py




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
