from django.contrib.auth.models import User
from django.db import models


# to conect ppl by there intersts
from django.urls import reverse


# Here I created products into the data bases
class WomenSkirtsProducts(models.Model):
    product_name = models.CharField(max_length=120)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name
