from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from . import serializers
from products import models

class CateGoryCreateView(ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    
    def get_queryset(self):
        return models.Category.objects.all()


class ProductCreateView(ListCreateAPIView):
    serializer_class = serializers.ProductSerializer
    filter_fields = ('category',)

    def get_queryset(self):
        return models.Product.objects.all()


class ProductRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = serializers.ProductSerializer

    def get_object(self):
        return models.Product.objects.get(pk=self.kwargs.get('pk', None))