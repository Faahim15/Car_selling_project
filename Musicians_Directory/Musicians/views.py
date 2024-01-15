from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from Musicians.models import MusicianModel 
from Musicians.forms import MusicianForm 
# Create your views here.


class MusiciansView(CreateView):
    model = MusicianModel 
    form_class = MusicianForm 
    template_name = 'add_musician.html' 
    success_url = reverse_lazy('homepage') 

class UpdateMusiciansView(UpdateView):
    model = MusicianModel 
    form_class = MusicianForm 
    template_name = 'add_musician.html' 
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage') 
    

