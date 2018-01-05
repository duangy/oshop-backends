from rest_framework import serializers
from products import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CartProductRelSerializer(serializers.Serializer):
    product = serializers.StringRelatedField()
    cart = serializers.StringRelatedField()
    quantity = serializers.IntegerField()


class ShoppingCartSerializer(serializers.ModelSerializer):
    products = CartProductRelSerializer(many=True, read_only=True)

    class Meta:
        model = models.ShoppingCart
        fields = '__all__'
    
    def create(self, validated_data):
        products_data = validated_data.pop('products') 
        cart = models.ShoppingCart.objects.create(**validated_data)
        all_products = []
        for product_data in products_data:
            all_products.append(models.CartProductRel(**product_data))
        models.CartProductRel.objects.bulk_create(all_products)
        return cart