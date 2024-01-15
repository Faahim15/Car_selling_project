from django.urls import path 
from .views import Register,Login,Logout,home,profile,change_pass,change_pass_without_oldPass
urlpatterns = [
  path('',home,name='homepage'),
  path('profile/',profile,name='profile'),
  path('profile/change_pass/',change_pass,name='change_pass'),
  path('profile/change_pass_without_oldPass/',change_pass_without_oldPass,name='change_pass_without_oldPass'),
  path('register',Register,name='register'),
  path('login/',Login,name='login'),
  path('logout/',Logout,name='logout'),

]