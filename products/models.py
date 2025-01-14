from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_models import BaseModel


class Product(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    price = models.DecimalField(verbose_name=_('price'), max_digits=12, decimal_places=4)
    code = models.CharField(verbose_name=_('code'), max_length=100, unique=True)
    is_active = models.BooleanField(verbose_name=_('is active'), default=True)

    def average_rating(self):
        ratings = self.ratings.all()
        return ratings.aggregate(avg_rating=models.Avg('rate')).get('avg_rating', 0)

    def __str__(self):
        return self.name


class Rating(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='ratings', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(verbose_name=_('rate'), default=0,
                                            validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"product: {self.product.name}, rate: {self.rate}"
