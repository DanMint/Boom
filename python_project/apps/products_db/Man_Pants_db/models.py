from django.contrib.auth.models import User
from django.db import models


# to conect ppl by there intersts
from django.urls import reverse


# Here I created products into the data bases
class ManPantsProducts(models.Model):
    product_name = models.CharField(max_length=120)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name

class Comment2(models.Model):
    user = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    product = models.ForeignKey(ManPantsProducts, on_delete=models.SET_NULL, null=True, related_name="comments")
    body = models.TextField()