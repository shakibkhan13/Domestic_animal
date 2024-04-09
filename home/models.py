from django.db import models
from django.contrib.auth.models import User
class Animal(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null = True , blank = True)
    Animal_name = models.CharField(max_length=100)
    Animal_Weight = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Prize = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Farm = models.CharField(max_length=100, default='Unknown')
    Animal_color = models.CharField(max_length=100, default='Unknown')
    Animal_description = models.TextField()
    Animal_image = models.ImageField(upload_to='animal_images', default='')

   