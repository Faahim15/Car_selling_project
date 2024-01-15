from django.db import models
from BrandApp.models import BrandModel 

# Create your models here. 
class CarModel(models.Model):
    title = models.CharField(max_length=80) 
    description = models.TextField() 
    image_field = models.ImageField(upload_to='CarApp/media/images/',blank = True, null = True)  
    quantity = models.PositiveIntegerField(blank= True, null = True)
    price = models.CharField(max_length=80, blank = True, null = True) 
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

