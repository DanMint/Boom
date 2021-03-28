from django.shortcuts import render
from .models import *
from python_project.apps.products_db.Man_DressShirts_db.models import ManDressShirtsProducts
from python_project.apps.products_db.Man_Pants_db.models import ManPantsProducts
from python_project.apps.products_db.Man_Shirts_db.models import ManShirtsProducts
from python_project.apps.products_db.Man_Sweater_db.models import MenSweatersProducts
from python_project.apps.products_db.Women_Dresses_db.models import WomenDressesProducts
from python_project.apps.products_db.Women_Pants_db.models import WomenPantsProducts
from python_project.apps.products_db.Women_Shirts_db.models import WomenShirtsProducts
from python_project.apps.products_db.Women_Skirts_db.models import WomenSkirtsProducts


def WomenShirtsForHTML(request):
    products = WomenShirtsProducts.objects.all()
    context = {'products': products}
    return render(request, 'products/Shirts/shirts.html', context)
