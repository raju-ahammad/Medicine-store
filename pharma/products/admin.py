from django.contrib import admin
from .models import Product, Ordering_Information, Specifications, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','time',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Ordering_Information)
admin.site.register(Specifications)
admin.site.register(Category)
# Register your models here.
