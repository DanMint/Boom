from django.urls import path

from . import views

app_name = "public"

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    # here we specify the data bases
    path('products/shirts', views.shirts, name="shirts"),
    path('products/pants', views.pants, name="pants"),
    path('products/dress', views.dress, name="dress"),
    path('products/skirts', views.skirts, name="skirts"),
    path('products/sweatshirts', views.swetshirts, name="swetshirts"),
    path('products/shirts/Givencci', views.Shirtone, name="Givencci"),

    # path('products/tankTops', views.tankTops),
    # path('products/socks', views.socks  ),
]