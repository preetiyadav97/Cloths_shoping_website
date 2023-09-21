from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index,name="index1"),
    path('contact/', views.contact,name="contact1"),
    path('about/', views.about,name="about1"),
    path('product/', views.product,name="product1"),
    path('single/', views.single,name="single1"),
    path('signup/', views.signup,name="signup1"),
    path('login/', views.login_detail,name="login1"),
    path('logout/', views.logout_detail,name="logout1"),
    path('nav/', views.nav),
    # path('payment/', views.payment),
    path('Cart/<int:pk>/', views.cart,name='cart'),
    path('cartshow/', views.cartshow,name='Cart'),
    path('purchase/', views.purchase,name='purchase'),
    path('total/<int:id>', views.total,name='total'),
    path('remove/<int:pk>', views.remove,name='remove'),
    path("add_to_cart/<int:pk>/", views.add_to_cart,name='add_to_cart'),
   
]