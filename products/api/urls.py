from django.urls import path
from products.api.views import ProductAPIView

app_name = "products"


urlpatterns = [
    path('product/<str:product_code>/', ProductAPIView.as_view(), name='product_api'),
]
