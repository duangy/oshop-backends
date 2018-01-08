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


class CartProductRelSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = models.CartProductRel
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex')
    cartproductrel_set = CartProductRelSerializer(many=True)

    class Meta:
        model = models.ShoppingCart
        fields = ('id', 'user', 'cartproductrel_set')
    
    def create(self, validated_data):
        products_data = validated_data.pop('products') 
        cart = models.ShoppingCart.objects.create(**validated_data)
        all_products = []
        for product_data in products_data:
            all_products.append(models.CartProductRel(**product_data))
        models.CartProductRel.objects.bulk_create(all_products)
        return cart