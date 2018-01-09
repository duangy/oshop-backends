from rest_framework import serializers
from products import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields ='__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')

    class Meta:
        model = models.ShoppingCart
        fields = '__all__'
