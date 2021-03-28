from django.shortcuts import render
from .models import *


def store(request):
    products = Products.objects.all()
    context = {'products ': products}
    return render(request, )
