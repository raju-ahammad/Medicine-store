from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Cart
from products.models import Product
from orders.models import Order
from Authentication.forms import LoginForm
from django.contrib.auth.decorators import login_required
from billing.models import BillingProfile
from adresse.forms import AddressForm
from adresse.models import Address


def cart_view(request):
    cart_obj, new_obj = Cart.objects.new_cart(request)
    return render(request, 'cart/cart.html', {'cart':cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show massage to user product is gone")
            return redirect('cart')
        cart_obj, new_obj = Cart.objects.new_cart(request)
        if product_obj in cart_obj.product.all():
            cart_obj.product.remove(product_obj)
        else:
            cart_obj.product.add(product_obj)
        request.session['cart_item'] = cart_obj.product.count()
    return redirect('cart')



def cheakout(request):
    cart_obj = Cart.objects.new_cart(request)
    cart_obj, cart_created = Cart.objects.new_cart(request)
    order_obj = None
    if cart_created or cart_obj.product.count() == 0:
        return redirect('cart')

    user = request.user
    billing_profile = None
    login_form = LoginForm()
    address_form = AddressForm()

    shipping_adress = request.session.get("shipping_adress_id", None)

    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)

    if billing_profile is not None:
        order_obj, order_ojbect_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_adress:
            order_obj.shipping_adress = Address.objects.get(id=shipping_adress)
            del request.session["shipping_adress_id"]
        if shipping_adress:
            order_obj.save()

    if request.method == 'POST':
        "some check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_item'] = 0
            del request.session['cart_id']
            return redirect("cheakout_done")



    context = {
          'cart' : cart_obj,
          'object' : order_obj,
          'billing_profile' : billing_profile,
          'login_form' : login_form,
          'address_form': address_form,

    }
    return render(request, "cart/checkout.html", context)


def cheakout_done_view(request):
    return render(request, "cart/thankyou.html", {})
