from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class Category(models.Model):
    name = models.CharField('名称', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = '产品分类'


class Product(models.Model):
    title = models.CharField('Title', max_length=20)
    price = models.FloatField('Price')
    category = models.ForeignKey(Category, verbose_name='Category')
    imageUrl = models.CharField('ImageUrl', max_length=255, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '产品信息'


class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products = models.ManyToManyField(Product, through='CartProductRel', through_fields=('cart', 'product'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = verbose_name_plural = '购物车'


class CartProductRel(models.Model):
    product = models.ForeignKey(Product, verbose_name='商品')
    cart = models.ForeignKey(ShoppingCart, verbose_name='购物车')
    quantity = models.IntegerField('数量', default=1)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = verbose_name_plural = '购物车商品'