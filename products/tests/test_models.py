import pytest

from products.models import Product, Rating


@pytest.mark.django_db
class TestProductModel:
    @pytest.fixture
    def setup_products_and_ratings(self, db):
        product1 = Product.objects.create(name="Mobile", price=10.00, code="P1")
        product2 = Product.objects.create(name="Laptop", price=25.00, code="P2")

        Rating.objects.create(product=product1, rate=4)
        Rating.objects.create(product=product1, rate=5)
        Rating.objects.create(product=product1, rate=3)

        Rating.objects.create(product=product2, rate=2)

        return product1, product2

    def test_product_str(self, setup_products_and_ratings):
        product1, product2 = setup_products_and_ratings
        assert str(product1) == "Mobile"
        assert str(product2) == "Laptop"

    def test_rating_str(self, setup_products_and_ratings):
        product1, _ = setup_products_and_ratings
        rating = Rating.objects.create(product=product1, rate=4)
        assert str(rating) == "product: Mobile, rate: 4"

    def test_average_rating(self, setup_products_and_ratings):
        product1, product2 = setup_products_and_ratings

        avg_rating_product1 = product1.average_rating()
        avg_rating_product2 = product2.average_rating()

        assert avg_rating_product1 == 4.0
        assert avg_rating_product2 == 2.0

    def test_average_rating_no_ratings(self):
        product = Product.objects.create(name="Product 3", price=30.00, code="P3")

        avg_rating = product.average_rating()

        assert avg_rating == 0.0
