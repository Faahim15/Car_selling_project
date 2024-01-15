from django.contrib import admin
from BrandApp.models import BrandModel 
from CarApp.models import CarModel 
from . import models
# Register your models here.

# admin.site.register(BrandModel)
admin.site.register(CarModel) 
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('brand_name',)}
    list_display = ['brand_name', 'slug']
    
admin.site.register(models.BrandModel, CategoryAdmin)