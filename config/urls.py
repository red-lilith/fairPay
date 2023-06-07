from django.urls import path, include


urlpatterns = [
    path("orders/", include("fairPay.orders.urls", namespace="orders")),

]