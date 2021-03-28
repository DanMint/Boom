from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request: HttpRequest) -> HttpResponse:
    # Here we can pass in data from our route to render the template
    print(request.user)
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")


def shirts(request: HttpRequest) -> HttpResponse:
    return render(request, "products/Shirts/shirts.html")


def pants(request: HttpRequest) -> HttpResponse:
    return render(request, "products/pants.html")


def Shirtone(request: HttpRequest) -> HttpResponse:
    return render(request, "products/Shirts/Things_shirts/ShirtOne.html")
