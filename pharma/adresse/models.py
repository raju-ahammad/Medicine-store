from django.db import models

# Create your models here.
from billing.models import BillingProfile


ADRESS_TYPE_CHOICES = (
             ('shipping', 'Shipping'),

)


ADRESS_CHOICES = (
       ('bangladesh', 'Bangladesh'),
       ('india', 'India'),
       ('america', 'America'),
       ('nepal', 'Nepal'),
       ('japan', 'Japan'),
       ('algeria', 'Algeria'),
)



class Address(models.Model):
    billing_profile  = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type     = models.CharField(max_length=120, null=True, blank=True, choices=ADRESS_TYPE_CHOICES)
    first_name       = models.CharField(max_length=120)
    last_name        = models.CharField(max_length=120)
    prescription     = models.ImageField(default='default.png', blank = True, null=True)
    country          = models.CharField(max_length=120, default='bangladesh', choices=ADRESS_CHOICES )
    adress_1         = models.CharField(max_length=120)
    adress_2         = models.CharField(max_length=120, null=True, blank=True)
    country_state    = models.CharField(max_length=120)
    post_or_zip      = models.CharField(max_length=120)
    email            = models.EmailField()
    phone            = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)
