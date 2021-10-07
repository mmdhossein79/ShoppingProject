from rest_framework import generics

from .serializers import ProductSerializer
from product.models import Product


class ProductAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
