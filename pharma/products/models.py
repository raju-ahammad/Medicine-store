
from django.db import models
from django.db.models.signals import pre_save, post_save
from pharma.utils import unique_slug_generator
from django.db.models import Q
from django.urls import reverse




# Create your models here.

class ProductQueryset(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)

    def search(self, query):
        looksup = Q(title__contains=query) | Q(description__contains=query) | Q(price__contains=query)
        return self.filter(looksup).distinct()



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()



    def active(self):
        return self.get_queryset().active()

    # def get_by_id(self, id):
    #     qs = self.get_queryset().filter(id=id)  #Product.objects == self.get_queryset()
    #     if qs.count() == 1:
    #         return qs.first()
    #     return None

    def search(self, query):
        return self.get_queryset().active().search(query)





class Category(models.Model):
    SUPPLEMENTS         = 'Supplements'
    VITAMINS            = 'Vitamins'
    NUTRITION           = 'Nutrition'
    TEACOFFE            = 'TeaCoffee'

    CATEGORY_NAME_CHOICE = (
        (SUPPLEMENTS, 'Supplements'),
        (VITAMINS, 'Vitamins'),
        (NUTRITION, 'Nutrition'),
        (TEACOFFE , 'TeaCoffee'),

    )
    name    = models.CharField(max_length=120, choices=CATEGORY_NAME_CHOICE, default=SUPPLEMENTS,)

class Ordering_Information(models.Model):
    material_1     = models.CharField(max_length=120)
    material_2     = models.CharField(max_length=120)
    material_3     = models.CharField(max_length=120)
    description_1  = models.CharField(max_length=300)
    description_2  = models.CharField(max_length=300)
    description_3  = models.CharField(max_length=300)
    packaging_1    = models.CharField(max_length=100)
    packaging_2    = models.CharField(max_length=100)
    packaging_3    = models.CharField(max_length=100)

    def __str__(self):
        return self.material_1


class Specifications(models.Model):
    hpis_code_1     =  models.CharField(max_length=100)
    hpis_code_2     =  models.CharField(max_length=100)
    hpis_code_3     =  models.CharField(max_length=100)
    S999_200_40_0_1 = models.CharField(max_length=100)
    S999_200_40_0_2 = models.CharField(max_length=100)
    S999_200_40_0_3 = models.CharField(max_length=100)

    def __str__(self):
        return self.hpis_code_1



class Product(models.Model):
    title         = models.CharField(max_length=120)
    slug          = models.SlugField(blank=True, null=True, unique=True)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description   = models.TextField()
    price         = models.DecimalField(max_digits=20, decimal_places=2, default=99.99)
    pre_price     = models.DecimalField(max_digits=20, decimal_places=2, default=99.99)
    image         = models.ImageField(default='default.png', blank = True, null=True)
    featured      = models.BooleanField(default=False)
    active        = models.BooleanField(default=True)
    ordering_information = models.ForeignKey(Ordering_Information, on_delete=models.CASCADE, null=True, blank=True)
    specifications  = models.ForeignKey(Specifications, on_delete=models.CASCADE, null=True, blank=True)
    time = models. DateTimeField(auto_now_add=True, null=True, blank=True)
    view = models.PositiveIntegerField(default = 0,blank=True,  null=True)


    class Meta():
        ordering = ('-time',)

    def get_absolute_url(self):
        return reverse('slug_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    objects = ProductManager()


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
