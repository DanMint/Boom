from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pip._vendor.requests import post

from python_project.apps.products_db.Man_Sweater_db.models import MenSweatersProducts
from python_project.apps.products_db.Women_Dresses_db.models import WomenDressesProducts, Comment, CommentForm
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


# def add_comment(request):
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.post = post
#         comment.save()
#         return render(request, "products/Dress/dress_comments.html")
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, "products/Dress/dress_comments.html", context)
#  return render(request, "products/Dress/dress_new_comment.html")
def add_comment(request: HttpRequest) -> HttpResponse:
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.user = "admin2"
        form.email = "lala@gmail.com"
        form.product = "Loro Piana"
        form.body = "haha"

    context = {'form':form}
    return render(request, "products/Dress/dress_new_comment.html", context)

    # new_comment = Comment()
    #
    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST or None)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save(commit=False)
    #         new_comment.post = post
    #         # Save the comment to the database
    #         new_comment.save()
    # else:
    #     comment_form = CommentForm()
    # return render(request, "products/Dress/dress_new_comment.html",
    #               {'post': post, 'new_comment': new_comment, 'comment_form': comment_form})
