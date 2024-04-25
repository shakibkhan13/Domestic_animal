from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='home'),
    path('home/', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('farm/', views.farm, name='farm'),
    path('checkout/', views.checkout, name='checkout'), 
    path('hospital/', views.hospital, name='hospital'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout_page'),
    path('register/', views.Register, name='register'),
    path('seller/', views.seller, name='seller'),
    path('cart/', views.cart, name='cart'),
    path('maps/', views.maps, name='maps'),
    path('delete-animal/<int:id>/', views.delete_animal, name="delete_animal"),
]
