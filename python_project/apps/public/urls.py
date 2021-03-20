from django.urls import path

from . import views

app_name = "public"

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('products/shirts', views.shirts, name="shirts"),
    path('products/pants', views.pants, name="pants"),
    # path('products/tankTops', views.tankTops),
    # path('products/socks', views.socks  ),
]
