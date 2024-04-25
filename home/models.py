
from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Animal_name = models.CharField(max_length=100)
    Animal_Weight = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Prize = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Farm = models.CharField(max_length=100, default='Unknown')
    Animal_color = models.CharField(max_length=100, default='Unknown')
    Animal_description = models.TextField()
    Animal_image = models.ImageField(upload_to='animal_images', default='')

class Customer(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200 ,null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200 , null=True)
    Price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)


    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)




class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)