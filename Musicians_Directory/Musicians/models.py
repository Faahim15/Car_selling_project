from django.db import models
from django.core.exceptions import ValidationError

def validate_phone_number_length(value):
    if len(value) != 11:
        raise ValidationError('Phone number must be 11 digits')

class MusicianModel(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=11, validators=[validate_phone_number_length])
    Instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return self.First_name