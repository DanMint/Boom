from django.urls import path

from . import views

app_name = "public"

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('products/f.shirts', views.shirts, name="shirts"),
    path('products/pants', views.pants, name="pants"),
    path('products/dress', views.dress, name="dress"),
    path('products/skirts', views.skirts, name="skirts"),
    path('products/m.shirts', views.mshirts, name="skirts"),
    path('products/t-shirts', views.tshirts, name="skirts"),
    path('products/sweatshirts', views.sweatshirts, name="skirts"),
    path('products/jeans', views.jeans, name="skirts"),
]
