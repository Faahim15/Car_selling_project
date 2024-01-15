from django.urls import path 
from . views import BrandModelView,DetailsCarView,buy_button_view,Order_history
urlpatterns = [

    path('add/',BrandModelView.as_view(),name='brand_details'),
    path('car_details/palce_order/<int:id>/',buy_button_view,name='place_order'),
    path('car_details/palce_order/order_history/',Order_history,name='order_history'),
    path('car_details/<int:id>/',DetailsCarView.as_view(),name='car_details'),
]