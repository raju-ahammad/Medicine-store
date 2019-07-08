from django.shortcuts import render, Http404,  get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView
from cart.models import Cart


# Create your views here.

class ProductListView(ListView):
    model   = Product
    template_name = 'product/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['product'] = Product.objects.all()
        context['popular'] = Product.objects.order_by('-view')[:6]
        return context


class ProductDetailView(DetailView):
    model    = Product
    template_name = 'product/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self):
        object = super(ProductDetailView, self).get_object()
        object.view += 1
        object.save()
        return object


class StoreListView(ListView):
    model   = Product
    template_name = 'product/store.html'
    def get_context_data(self, *args, **kwargs):
        context = super(StoreListView, self).get_context_data(*args, **kwargs)
        context['product'] = Product.objects.all()
        context['popular'] = Product.objects.order_by('-view')
        return context



class SlugDetailView(DetailView):
    model    = Product
    template_name = 'product/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SlugDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_cart(self.request)
        context['cart'] = cart_obj
        return context


    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug, active=True)
        return instance
