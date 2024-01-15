from django.contrib import admin
from .models import AlbumModel 
from Musicians.models import MusicianModel
# Register your models here.

admin.site.register(AlbumModel)
admin.site.register(MusicianModel)