from django.contrib.auth.models import User
from django.db import models

# to conect ppl by there intersts
from django.urls import reverse


class Products(models.Model):
    product_name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    price = models.CharField(max_length=120)
