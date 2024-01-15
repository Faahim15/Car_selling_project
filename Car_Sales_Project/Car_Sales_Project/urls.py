
from django.contrib import admin
from django.urls import path,include 
from . views import Home,UserLoginView,CustomLogoutView,RegistrationView,edit_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(), name = 'homepage'),
    path('category/<slug:category_slug>/', Home.as_view(), name='category_wise_post'), 
    path('profile/edit',edit_profile,name='edit_profile'),
    path('login/',UserLoginView.as_view(), name = 'login'), 
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/',RegistrationView.as_view(), name = 'register'),
    path('brand/',include('BrandApp.urls')),
    path('car/',include('CarApp.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)