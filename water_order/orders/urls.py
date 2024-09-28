
from django.urls import path
from .views import order_water

urlpatterns = [
    path('', order_water, name='order_water'),
]
