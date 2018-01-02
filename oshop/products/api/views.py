from rest_framework.generics import ListCreateAPIView
from . import serializers
from products import models

class CateGoryCreateView(ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    
    def get_queryset(self):
        return models.Category.objects.all()


class ProductCreateView(ListCreateAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.Product.objects.all()