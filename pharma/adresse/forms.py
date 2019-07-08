from  django import forms

from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ( 'first_name',
                   'last_name',
                   'country',
                   'adress_1',
                   'adress_2',
                   'country_state',
                   'post_or_zip',
                   'email',
                   'phone',
                  )
