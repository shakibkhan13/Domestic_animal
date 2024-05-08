
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Animal(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Animal_name = models.CharField(max_length=100)
    Animal_Weight = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Prize = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Farm = models.CharField(max_length=100, default='Unknown')
    Animal_color = models.CharField(max_length=100, default='Unknown')
    Animal_description = models.TextField()
    Animal_image = models.ImageField(upload_to='animal_images', default='')
    quantity = models.PositiveIntegerField(default=1)  

    def __str__(self):
        return self.Animal_name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name if self.name is not None else ""




class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    Price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        return sum(Animal.get_total for Animal in orderitem)

    @property
    def get_cart_animal(self):
        orderitem = self.orderitem_set.all()
        return sum(Animal.quantity for Animal in orderitem)


class OrderItem(models.Model):
    Animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.Animal.Animal_Prize * self.quantity



class ShippingAddress(models.Model): 
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.address
