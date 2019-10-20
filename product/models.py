from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.db.models import Q
from django.urls import reverse





class ProductQueryset(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)

    def search(self, query):
        looksup = Q(name__contains=query) | Q(description__contains=query) | Q(price__contains=query)
        return self.filter(looksup).distinct()



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()



    def active(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().active().search(query)


class Category(models.Model):
    MENS_JEANS      = 'Mens Jeans'
    MENS_TSHIRT     = 'Mens Tshirt'
    MENS_WATCH      = 'Mens Watch'
    MENS_SNEAKER    = 'MEN’S SNEAKER'
    WOMENS_JEANS    = 'WoMens Jeans'
    WOMENS_TSHIRT   = 'WoMens Tshirt'
    WOMENS_WATCH    = 'WoMens Watch'
    WOMENS_PARSE    = 'WoMens Parse'
    WOMENS_SNEAKER  = 'WOMEN’S SNEAKER'

    CATEGORY_CHOICE = (
        (MENS_JEANS , 'Mens Jeans'),
        (MENS_TSHIRT,  'Mens Tshirt'),
        (MENS_WATCH, 'Mens Watch'),
        (MENS_SNEAKER, 'MEN’S SNEAKER'),
        (WOMENS_JEANS, 'WoMens Jeans'),
        (WOMENS_TSHIRT,'WoMens Tshirt'),
        (WOMENS_WATCH ,'WoMens Watch'),
        (WOMENS_PARSE, 'WoMens Parse'),
        (WOMENS_SNEAKER, 'WOMEN’S SNEAKER')
    )
    name = models.CharField(max_length=120, choices=CATEGORY_CHOICE, blank=True, null=True, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering         = ('name',)
        verbose_name     = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Product(models.Model):
    INSTOCK      = 'instock'
    STOCKOUT      = 'stockout'
    AVAILABLE_CHOICE = (
        (INSTOCK, 'instock'),
        (STOCKOUT, 'stockout')
    )
    name           = models.CharField(max_length=100)
    slug           = models.SlugField(blank=True, null=True, unique=True)
    price          = models.FloatField()
    pre_price      = models.FloatField(blank=True, null=True)
    available      = models.CharField(max_length=120, choices=AVAILABLE_CHOICE, default=INSTOCK)
    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now=True)
    featured       = models.BooleanField(default=False)
    inspired       = models.BooleanField(default=False)
    active         = models.BooleanField(default=True)
    preview_text   = models.TextField()
    description    = models.TextField()
    category       = models.ForeignKey(Category, on_delete=models.CASCADE)
    image          = models.ImageField(blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)



    class Meta():
        ordering = ('-created',)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug': self.slug})

    objects = ProductManager()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image.url




def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(category_pre_save_receiver, sender=Category)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
