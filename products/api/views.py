from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.api.serializers import ProductSerializer
from products.crawler import crawl_amazon
from products.models import Product


class ProductAPIView(APIView):
    def get(self, request, product_code):
        cache_key = f"product_{product_code}"
        cached_product = cache.get(cache_key)
        if cached_product:
            return Response(cached_product, status=status.HTTP_200_OK)

        try:
            product = Product.objects.get(product_code=product_code)
            serializer = ProductSerializer(product)
            cache.set(cache_key, serializer.data, timeout=3600)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            pass

        try:
            product_data = crawl_amazon(product_code)
            product = Product.objects.create(product_code=product_code, **product_data)
            serializer = ProductSerializer(product)
            cache.set(cache_key, serializer.data, timeout=3600)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
