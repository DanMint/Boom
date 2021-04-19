from django.contrib import admin
from django.template.defaulttags import comment

from .models import Order, OrderItem, ShippingAddress, Customer
from python_project.apps.products_db.Man_DressShirts_db.models import ManDressShirtsProducts
from python_project.apps.products_db.Man_Pants_db.models import ManPantsProducts
from python_project.apps.products_db.Man_Shirts_db.models import ManShirtsProducts
from python_project.apps.products_db.Man_Sweater_db.models import MenSweatersProducts
from python_project.apps.products_db.Women_Dresses_db.models import WomenDressesProducts, Comment
from python_project.apps.products_db.Women_Pants_db.models import WomenPantsProducts
from python_project.apps.products_db.Women_Shirts_db.models import WomenShirtsProducts
from python_project.apps.products_db.Women_Skirts_db.models import WomenSkirtsProducts

admin.site.register(Customer)
admin.site.register(WomenShirtsProducts)
admin.site.register(WomenSkirtsProducts)
admin.site.register(WomenPantsProducts)
admin.site.register(WomenDressesProducts)
admin.site.register(MenSweatersProducts)
admin.site.register(ManShirtsProducts)
admin.site.register(ManPantsProducts)
admin.site.register(ManDressShirtsProducts)
admin.site.register(Comment)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

