from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('checkout/address/create/', views.checkout_address_create_view, name='checkout_address_create'),
]


urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
