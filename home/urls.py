from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal),
    path('Home/', views.Home, name='home'), 
    path('blogs/', views.blogs, name='blogs'),
    path('farm/', views.farm, name='farm'),
    path('hospital/', views.hospital, name='hospital'),
    path('login/', views.login, name='login'),
    path('seller/', views.seller, name='seller'),
    path('cart/', views.cart, name='cart'), 
]
