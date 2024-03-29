from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from .forms import AddressForm
from billing.models import BillingProfile

def checkout_address_create_view(request):
    form  = AddressForm(request.POST or None)
    context = {
               "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        print(request.POST)
        user = request.user
        instance = form.save(commit=False)
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)
        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()

            #request.session[address_type + "_address_id"] = instance.id
            request.session["shipping_adress_id"] = instance.id
            #print(address_type + "_address_id")
        else:
            print("Error here")
            return redirect(redirect_path)

        if is_safe_url(redirect_path, request.get_host()):
            return redirect('cheakout')
        else:
            return redirect('cheakout')
    else:
        return redirect('cheakout')
