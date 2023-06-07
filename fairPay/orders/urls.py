from django.urls import path
from .views import *


app_name = "orders"
urlpatterns = [
    path('update-orders', delete_orders),
    path('get-orders', get_orders)
]
