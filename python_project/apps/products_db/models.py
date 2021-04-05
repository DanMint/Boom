from django.contrib.auth.models import User
from django.db import models

# to conect ppl by there intersts
from django.urls import reverse

from python_project.apps.products_db.Man_DressShirts_db.models import ManDressShirtsProducts
from python_project.apps.products_db.Man_Pants_db.models import ManPantsProducts
from python_project.apps.products_db.Man_Shirts_db.models import ManShirtsProducts
from python_project.apps.products_db.Man_Sweater_db.models import MenSweatersProducts
from python_project.apps.products_db.Women_Dresses_db.models import WomenDressesProducts
from python_project.apps.products_db.Women_Pants_db.models import WomenPantsProducts
from python_project.apps.products_db.Women_Shirts_db.models import WomenShirtsProducts
from python_project.apps.products_db.Women_Skirts_db.models import WomenSkirtsProducts


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    # in order we need to remember that every order has to be to a specific customer
    # if the customer gets deleted then we set to null
    # rememebr the User is a many to one relation meaning that we can have alot of things connected to it
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    # if complete is false we can put more things into it
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


# WomenShirtsProducts, WomenSkirtsProducts, WomenPantsProducts, WomenDressesProducts,MenSweatersProducts, ManShirtsProducts, ManPantsProducts, ManDressShirtsProducts,

class OrderItem(models.Model):
    Women_Shirts_product = models.ForeignKey(WomenShirtsProducts, on_delete=models.SET_NULL, null=True, blank=True)
    Women_Skirts_product = models.ForeignKey(WomenSkirtsProducts, on_delete=models.SET_NULL, null=True, blank=True)
    Women_Pants_product = models.ForeignKey(WomenPantsProducts, on_delete=models.SET_NULL, null=True, blank=True)
    Women_Dresses_product = models.ForeignKey(WomenDressesProducts, on_delete=models.SET_NULL, null=True, blank=True)
    Mans_Sweaters_product = models.ForeignKey(MenSweatersProducts, on_delete=models.SET_NULL, null=True, blank=True)
    Mans_Shirts_product = models.ForeignKey(ManShirtsProducts, on_delete=models.SET_NULL, null=True, blank=True)
    Mans_Pants_product = models.ForeignKey(ManPantsProducts, on_delete=models.SET_NULL, null=True, blank=True)
    Mans_DressShirts_product = models.ForeignKey(ManDressShirtsProducts, on_delete=models.SET_NULL, null=True,
                                                 blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipCode = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.address
