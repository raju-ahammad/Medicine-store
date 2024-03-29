from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('cheakout/', views.cheakout, name='cheakout'),
    path('cart_update/', views.cart_update, name='cart_update'),
    path('cheakout/done', views.cheakout_done_view, name='cheakout_done'),
]
