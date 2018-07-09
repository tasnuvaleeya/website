from django.contrib import admin
from .models import Album, Song


my_models = [Album, Song]
admin.site.register(my_models)
