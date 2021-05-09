from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from python_project.apps.products_db.Man_Sweater_db.models import MenSweatersProducts
from python_project.apps.products_db.Women_Dresses_db.models import WomenDressesProducts, Comment
from python_project.apps.products_db.Women_Pants_db.models import WomenPantsProducts
from python_project.apps.products_db.Women_Shirts_db.models import WomenShirtsProducts
from python_project.apps.products_db.Women_Skirts_db.models import WomenSkirtsProducts
from python_project.apps.products_db.models import Order


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


def dress(request):
    products = WomenDressesProducts.objects.all()
    context = {'products': products}
    return render(request, 'products/Dress/dress.html', context)


def skirts(request):
    products = WomenSkirtsProducts.objects.all()
    context = {'products': products}
    return render(request, 'products/Skirts/skirts.html', context)


def pants(request: HttpRequest) -> HttpResponse:
    products = WomenPantsProducts.objects.all()
    context = {'products': products}
    return render(request, 'products/Skirts/skirts.html', context)


def sweatshirts(request: HttpRequest) -> HttpResponse:
    products = MenSweatersProducts.objects.all()
    context = {'products': products}
    return render(request, 'products/Skirts/skirts.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


def dress_comments(request: HttpRequest) -> HttpResponse:
    items = Comment.objects.all()
    context = {'items': items}
    return render(request, "products/Dress/dress_comments.html", context)


def add_comment(request):
    post = None
    print('0')
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get(
                'body'):
            print("1")
            post = Comment()
            print("2")
            post.user = request.POST.get('user')
            print("3")
            post.email = request.POST.get('email')
            print("4")
            post.product = request.POST.get('product')
            print("5")
            post.body = request.POST.get('body')
            print("6")
            post.save()
            print("7")

    return render(request, "products/Dress/dress_new_comment.html",
                  {'post': post})


def adm(request: HttpRequest) -> HttpResponse:
    commo = Comment.objects.all()
    dresses = WomenDressesProducts.objects.all()
    context = {'comments': commo, 'dress': dresses}
    return render(request, "admin2.html", context)


def delete_comment_for_admin(request, id):
    print(1)
    deleto = Comment.objects.get(id=id)
    print(2)
    deleto.delete()
    print(3)
    return render(request, "delete_view.html")