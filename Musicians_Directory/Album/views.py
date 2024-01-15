from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import AlbumModel 
from .forms import AlbumForm 
from Musicians.models import MusicianModel
from django.urls import reverse_lazy
# Create your views here.


class AlbumView(CreateView):
    model = AlbumModel 
    form_class = AlbumForm 
    template_name = 'add_album.html' 
    success_url = reverse_lazy('homepage')

class UpadateAlbumView(UpdateView):
    model = AlbumModel 
    form_class = AlbumForm 
    template_name = 'add_album.html'  
    pk_url_kwarg = 'id' 
    success_url = reverse_lazy('homepage')

class DeleteAlbumView(DeleteView):
    model = MusicianModel
    pk_url_kwarg = 'id'
    template_name = 'delete.html' 
    success_url = reverse_lazy('homepage')
    