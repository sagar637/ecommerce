from django.urls import path 

from .views import index 

from django.urls import path
from .views import error_page, cart, removecart, success_page, error_page


urlpatterns = [
    path('', index),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('error_page/', error_page, name="error_page"),
    path('success_page/',success_page,name="success_page")
]
