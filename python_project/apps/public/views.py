from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from python_project.apps.products_db.Women_Shirts_db.models import WomenShirtsProducts


def index(request: HttpRequest) -> HttpResponse:
    # Here we can pass in data from our route to render the template
    print(request.user)
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")


def shirts(request):
    products = WomenShirtsProducts.objects.all()
    context = {'products': products}
    return render(request, 'products/Shirts/shirts.html', context)


def dress(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/Dress/dress.html')


def skirts(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/Skirts/skirts.html')


def pants(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/Pants/pants.html')


def sweatshirts(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/SweatShirts/sweatshirts.html')
