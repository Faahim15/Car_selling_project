from django.shortcuts import render
from django.views.generic import CreateView  
from django.urls import reverse_lazy
from . models import CarModel
from . forms import CarModelForm
# Create your views here.
class CarModelView(CreateView):
    model = CarModel 
    form_class = CarModelForm 
    template_name = 'add_car.html' 
    context_object_name = 'form' 
    success_url = reverse_lazy('cardetails')
    