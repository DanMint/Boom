from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from python_project.apps.products_db.Man_DressShirts_db.models import Comment1
from python_project.apps.products_db.Man_Pants_db.models import Comment2
from python_project.apps.products_db.Man_Shirts_db.models import Comment3
from python_project.apps.products_db.Man_Sweater_db.models import MenSweatersProducts, Comment4
from python_project.apps.products_db.Women_Dresses_db.models import WomenDressesProducts, Comment
from python_project.apps.products_db.Women_Pants_db.models import WomenPantsProducts, Comment5
from python_project.apps.products_db.Women_Shirts_db.models import WomenShirtsProducts, Comment6
from python_project.apps.products_db.Women_Skirts_db.models import WomenSkirtsProducts, Comment7
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

def mendressshirts_comments1(request: HttpRequest) -> HttpResponse:
    items = Comment1.objects.all()
    context = {'items': items}
    return render(request, "products/ManDressShirts/manDressShirts_comments1.html", context)

def menpants_comments2(request: HttpRequest) -> HttpResponse:
    items = Comment2.objects.all()
    context = {'items': items}
    return render(request, "products/ManPants/manPants_comments2.html", context)

def menshirts_comments3(request: HttpRequest) -> HttpResponse:
    items = Comment3.objects.all()
    context = {'items': items}
    return render(request, "products/ManShirts/manShirts_comments3.html", context)

def mensweater_comments4(request: HttpRequest) -> HttpResponse:
    items = Comment4.objects.all()
    context = {'items': items}
    return render(request, "products/ManSweater/manSweater_comments4.html", context)

def womendress_comments(request: HttpRequest) -> HttpResponse:
    items = Comment.objects.all()
    context = {'items': items}
    return render(request, "products/WomenDress/womenDress_comments.html", context)

def womenpants_comments5(request: HttpRequest) -> HttpResponse:
    items = Comment5.objects.all()
    context = {'items': items}
    return render(request, "products/WomenPants/womenPants_comments5.html", context)

def womenshirts_comments6(request: HttpRequest) -> HttpResponse:
    items = Comment6.objects.all()
    context = {'items': items}
    return render(request, "products/WomenShirts_comments6/WomenShirts_comments6.html", context)

def womenskirts_comments7(request: HttpRequest) -> HttpResponse:
    items = Comment7.objects.all()
    context = {'items': items}
    return render(request, "products/WomenSkirts_comments6/WomenSkirts_comments7.html", context)

def add_comment1(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/ManDressShirts/manDressShirts_new_comment.html",
                  {'post': post})

def add_comment2(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/ManPants/manPants_new_comment.html",
                  {'post': post})

def add_comment3(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/ManShirts/manShirts_new_comment.html",
                  {'post': post})

def add_comment4(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/ManSweater/manSweater_new_comment.html",
                  {'post': post})

def add_comment(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/Dress/womanDress_new_comment.html",
                  {'post': post})

def add_comment5(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/WomenPants/womenPants_new_comment.html",
                  {'post': post})

def add_comment6(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/WomenShirts/womenShirts_new_comment.html",
                  {'post': post})

def add_comment7(request):
    post = None
    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('product') and request.POST.get('body'):
            post = Comment()
            post.user = request.POST.get('user')
            post.email = request.POST.get('email')
            post.product = request.POST.get('product')
            post.body = request.POST.get('body')
            post.save()

    return render(request, "products/WomanSkirts/womanSkirts_new_comment.html",
                  {'post': post})
