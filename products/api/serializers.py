from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'rate', 'price', 'is_active', 'created_time', 'updated_time']

    def get_rate(self, obj):
        return obj.average_rating()
