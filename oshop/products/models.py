from django.db import models

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