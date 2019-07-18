from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.ProductListView.as_view(), name= 'home'),
    path('home/', views.ProductListView.as_view(), name= 'home'),
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name= 'detail'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('store/', views.StoreListView.as_view(), name= 'store'),
    path('detail/<slug:slug>', views.SlugDetailView.as_view(), name= 'slug_detail'),
    path('about/', views.AboutUs.as_view(), name= 'about'),
    path('contact/', views.AboutUs.as_view(), name= 'contact'),


]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
