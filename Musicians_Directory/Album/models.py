from django import forms
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Musicians.models import MusicianModel

class AlbumModel(models.Model):
    VALUE_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five')
    ]

    album_name = models.CharField(max_length=50)
    album_release_date = models.DateField()
    album_rating = models.IntegerField(choices=VALUE_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    musicians = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name