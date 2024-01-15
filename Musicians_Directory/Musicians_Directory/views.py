from django.views.generic import ListView, CreateView 
from django.contrib.auth.views import LoginView,LogoutView
from Album.models import AlbumModel 
from django.contrib.auth.models import User 
from . forms import RegistrationForm 
from django.urls import reverse_lazy 
from django.contrib import messages 
from django.contrib.auth import logout 
from django.shortcuts import redirect
from django.views import View

class ShowingAllObejectsView(ListView):
    model = AlbumModel 
    template_name = 'home.html' 
    context_object_name = 'data' 

class RegistrationView(CreateView):
    model = User 
    form_class = RegistrationForm 
    template_name = 'register.html' 
    success_url = reverse_lazy('Login') 
    context_object_name = 'form' 

class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
    

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('homepage')