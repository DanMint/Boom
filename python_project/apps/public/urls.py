from django.urls import path

from . import views

app_name = "public"

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('cart', views.cart, name="cart"),
    path('admino', views.adm, name = 'admin'),
    path('products/dress/comments', views.dress_comments, name="dress_comment"),
    path('products/dress/add_comment', views.add_comment, name="add_dress_comment"),
    # here we specify the data bases
    path('products/shirts', views.shirts, name="shirts"),
    path('products/pants', views.pants, name="pants"),
    path('products/dress', views.dress, name="dress"),
    path('products/skirts', views.skirts, name="skirts"),
    path('products/sweatshirts', views.sweatshirts, name="sweatshirts"),
    # path('products/tankTops', views.tankTops),
    # path('products/socks', views.socks  ),
    path('delete/<int:id>', views.delete_comment_for_admin, name='deletion'),
]
