
from django.urls import path
from Album.views import AlbumView,DeleteAlbumView,UpadateAlbumView
urlpatterns = [
    path('add/',AlbumView.as_view(), name='add_album'),
    path('edit/<int:id>', UpadateAlbumView.as_view(), name='edit_album'),
    path('delete/<int:id>',DeleteAlbumView.as_view(),name='delete_musician'),
]