from rest_framework import serializers

from product.models import Product


# User Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Register Serializer
