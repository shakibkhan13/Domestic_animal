from django.contrib import admin
from .models import Animal, Order, ShippingAddress, Customer

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('Animal_name', 'Animal_Weight', 'Animal_Prize', 'Animal_Farm', 'Animal_color')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount', 'date_ordered')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'address', 'city')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'User')
