
from django.contrib import admin
from django.urls import path,include 
from .views import ShowingAllObejectsView,RegistrationView,UserLoginView,CustomLogoutView
from django.contrib.auth.views import LogoutView
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('',ShowingAllObejectsView.as_view(), name = 'homepage'),
    path('login/',UserLoginView.as_view(), name = 'Login'), 
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/',RegistrationView.as_view(), name = 'register'),
    path('musician/',include('Musicians.urls')),
    path('album/',include('Album.urls')),
]
