from decimal import Decimal

import pytest
from django.core.cache import cache
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from products.models import Product


@pytest.mark.django_db
class TestProductAPIView:
    def setup_method(self):
        self.client = APIClient()

    def test_get_product_from_cache(self, monkeypatch):
        cache_key = "product_P1"
        cache.set(cache_key, {'name': 'Product 1', 'price': 100.00, 'code': 'P1', 'is_active': True}, timeout=3600)

        response = self.client.get(reverse('products:product_api', args=['P1']))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Product 1'

    def test_get_product_from_database(self):
        product = Product.objects.create(name="Product 2", price=Decimal('150.0000'), code="P2", is_active=True)

        response = self.client.get(reverse('products:product_api', args=['P2']))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == product.name
        assert Decimal(response.data['price']) == product.price

    def test_create_product_by_crawling_amazon(self, monkeypatch):
        def mock_crawl_amazon(product_code):
            return {
                'name': 'Mocked Product',
                'price': '99.99',
            }

        monkeypatch.setattr('products.api.views.crawl_amazon', mock_crawl_amazon)

        response = self.client.get(reverse('products:product_api', args=['P3']))
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'Mocked Product'

        product = Product.objects.get(code='P3')
        assert product.name == 'Mocked Product'
        assert Decimal(response.data['price']) == product.price

    def test_product_not_found(self, monkeypatch):
        def mock_crawl_amazon(product_code):
            raise ValueError("Product not found on Amazon")

        monkeypatch.setattr('products.api.views.crawl_amazon', mock_crawl_amazon)

        response = self.client.get(reverse('products:product_api', args=['P4']))
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data['error'] == "Product not found on Amazon"
