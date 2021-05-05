from django.urls import path

from . import views

app_name = "public"

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('cart', views.cart, name="cart"),
    path('products/mandressshirts/comments1', views.mandressshirts_comments1, name="manDressShirts_comment1"),
    path('products/mandressshirts/add_comment1', views.add_comment1, name="add_manDressShirts_comment1"),
    path('products/manpants/comments2', views.manpants_comments2, name="manDressShirts_comment2"),
    path('products/manpants/add_comments2', views.add_comment2, name="add_manDressShirts_comment2"),
    path('products/manshirts/comments3', views.manshirts_comments3, name="manShirts_comment3"),
    path('products/manshirts/add_comment3', views.add_comment3, name="add_manShirts_comment3"),
    path('products/mansweater/comments4', views.mansweater_comments4, name="manSweater_comment4"),
    path('products/mansweater/add_comments4', views.add_comment4, name="add_manSweater_comment4"),
    path('products/womendress/comments', views.womendress_comments, name="womenDress_comment"),
    path('products/womendress/add_comment', views.add_comment, name="add_womenDress_comment"),
    path('products/womenpants/comments5', views.womenpants_comments5, name="womenPants_comment5"),
    path('products/womenpants/add_comment5', views.add_comment5, name="add_womenPants_comment5"),
    path('products/womenshirts/comments6', views.womenshirts_comments6, name="womenShirts_comment6"),
    path('products/womenshirts/add_comments6', views.add_comment6, name="add_womenShirts_comment6"),
    path('products/womenskirts/comments7', views.womenskirts_comments7, name="womenSkirts_comment7"),
    path('products/womenskirts/add_comment7', views.add_comment7, name="add_womenSkirts_comment7"),
    # here we specify the data bases
    path('products/shirts', views.shirts, name="shirts"),
    path('products/pants', views.pants, name="pants"),
    path('products/dress', views.dress, name="dress"),
    path('products/skirts', views.skirts, name="skirts"),
    path('products/sweatshirts', views.sweatshirts, name="sweatshirts"),
    # path('products/tankTops', views.tankTops),
    # path('products/socks', views.socks  ),
]
