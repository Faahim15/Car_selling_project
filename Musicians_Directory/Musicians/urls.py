
from django.urls import path
from Musicians.views import MusiciansView,UpdateMusiciansView
urlpatterns = [
    path('add/',MusiciansView.as_view(), name='add_musician'),
    path('edit/<int:id>', UpdateMusiciansView.as_view(), name='edit_musician'),
]