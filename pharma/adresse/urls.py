from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('checkout/address/create/', views.checkout_address_create_view, name='checkout_address_create'),
]
