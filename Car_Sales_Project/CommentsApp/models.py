from django.db import models
from CarApp.models import CarModel 
from CarApp.models import CarModel 
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.


class Comment(models.Model):
    cars = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"

class Order (models.Model):
    car = models.ForeignKey(CarModel, on_delete = models.CASCADE) 
    customer = models.ForeignKey(User, on_delete = models.CASCADE) 
    order_date =models.DateTimeField(default =timezone.now)