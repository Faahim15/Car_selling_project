from django.urls import path 
from CarApp.views import CarModelView
urlpatterns = [

    path('add/',CarModelView.as_view(),name='cardetails'),
]