
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('Authentication.urls')),
    path('', include('cart.urls')),
    path('', include('orders.urls')),
    path('', include('adresse.urls')),
    path('', include('search.urls')),


    path('user/', include('django.contrib.auth.urls')),
]
