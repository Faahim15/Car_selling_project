from django.shortcuts import render,redirect 
from django.views.generic import CreateView 
from . forms import RegistrationForm 
from django.contrib.auth.models import User 
from django.urls import reverse_lazy 
from django.contrib import messages 
from django.contrib.auth.views import LoginView 
from django.views.generic import ListView
from django.views import View 
from django.contrib.auth import logout 
from CarApp.models import CarModel 
from BrandApp.models import BrandModel 
from . import forms

# def home (request):
#     return render(request, 'home.html')  

class Home(ListView):
    model = CarModel 
    template_name = 'home.html' 
    context_object_name = 'data' 
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
         category = BrandModel.objects.get(slug=category_slug)
         return CarModel.objects.filter(brand=category) 
        else:
         return CarModel.objects.all() 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = BrandModel.objects.all()
        return context


class RegistrationView(CreateView):
    model = User 
    form_class = RegistrationForm 
    template_name = 'signup.html' 
    success_url = reverse_lazy('login') 
    context_object_name = 'form' 

class UserLoginView(LoginView):
    template_name = 'signup.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('order_history')
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
        messages.success(self.request, 'Successful Logged Out ')
        return redirect('homepage')  
    
# def Profile(request):
#     return render(request, 'profile.html')


def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('order_history')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})