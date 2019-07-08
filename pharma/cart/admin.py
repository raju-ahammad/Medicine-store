from django.contrib import admin
from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'total', )
admin.site.register(Cart, CartAdmin)
