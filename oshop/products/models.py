from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('名称', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = '产品分类'