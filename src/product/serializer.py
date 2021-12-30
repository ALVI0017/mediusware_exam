from rest_framework.serializers import ModelSerializer
from .models import *


class productSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','sku','description','created_at','updated_at']
        
        
# class productVariant(ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'title','sku','description','created_at','updated_at']