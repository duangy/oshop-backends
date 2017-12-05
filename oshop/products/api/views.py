from rest_framework.generics import ListCreateAPIView
from . import serializers
from products import models

class CateGoryCreateView(ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    
    def get_queryset(self):
        return models.Category.objects.all()