from django.contrib.auth.models import User
from django.db import models
from python_project.apps.accounts.models import UserProfile

# to conect ppl by there intersts
from django.urls import reverse


# Here I created products into the data bases
class Products(models.Model):
    product_name = models.CharField(max_length=120)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    # image = models.ImageField()

    def __str__(self):
        return self.product_name


class Order(models.Model):
    # in order we need to remember that every order has to be to a specific customer
    # if the customer gets deleted then we set to null
    # rememebr the User is a many to one relation meaning that we can have alot of things connected to it
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    # if complete is false we can put more things into it
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipCode = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.address
