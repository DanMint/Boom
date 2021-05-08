from django.urls import path

from . import views

app_name = "public"

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('cart', views.cart, name="cart"),
    path('products/mendressshirts/comments1', views.mendressshirts_comments1, name="menDressShirts_comment1"),
    path('products/mendressshirts/add_comment1', views.add_comment1, name="add_menDressShirts_comment1"),
    path('products/menpants/comments2', views.menpants_comments2, name="menDressShirts_comment2"),
    path('products/menpants/add_comments2', views.add_comment2, name="add_menDressShirts_comment2"),
    path('products/menshirts/comments3', views.mendressshirts_comments3, name="menShirts_comment3"),
    path('products/menshirts/add_comment3', views.add_comment3, name="add_menShirts_comment3"),
    path('products/mensweater/comments4', views.menpants_comments4, name="menSweater_comment4"),
    path('products/mensweater/add_comments4', views.add_comment4, name="add_menSweater_comment4"),
    path('products/womendress/comments', views.womendress_comments, name="womenDress_comment"),
    path('products/womendress/add_comment', views.add_comment, name="add_womenDress_comment"),
    path('products/womenpants/comments5', views.mendressshirts_comments5, name="womenPants_comment5"),
    path('products/womenpants/add_comment5', views.add_comment5, name="add_womenPants_comment5"),
    path('products/womenshirts/comments6', views.menpants_comments6, name="womenShirts_comment6"),
    path('products/womenshirts/add_comments6', views.add_comment6, name="add_womenShirts_comment6"),
    path('products/womenskirts/comments7', views.womendress_comments7, name="womenSkirts_comment7"),
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
