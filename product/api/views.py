from django.core.paginator import Paginator
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductSerializer
from product.models import Product

class ProductPagenation(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'




class ProductAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagenation
    # def get_queryset(self):
    #     all_products = Product.objects.all().order_by("-id")
    #     paginator = Paginator(all_products, 1)
    #     page_number = self.request.GET.get('page')
    #     print(page_number)
    #     product_list = paginator.get_page(page_number)
    #     context['page_obj'] = product_list
