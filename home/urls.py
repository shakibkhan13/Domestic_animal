from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal, name='home'),
    #path('', views.Home, name='home'), 
    path('blogs/', views.blogs, name='blogs'),
    path('farm/', views.farm, name='farm'),
    path('hospital/', views.hospital, name='hospital'),
    path('login/', views.login, name='login'),
    path('seller/', views.seller, name='seller'),
    path('cart/', views.cart, name='cart'), 
    path('maps/',views.maps ,name='maps'),
    path('delete-animal/<int:id>/', views.delete_animal, name="delete_animal")
]
