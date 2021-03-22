from django.contrib.auth.models import User
from django.db import models

# to conect ppl by there intersts
from django.urls import reverse


# every product needs to have its guid and when the user will be adding products into the cart
# the front end service will store the products in an array of guids
# to google: django guid, django make dynamic page for product with guid, django make shop cart
class Products(models.Model):
    product_name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    # models.IntegerField
    price = models.CharField(max_length=120)
    # here we create a field called image
    # inevtory
