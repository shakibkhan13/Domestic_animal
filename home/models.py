from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Animal(models.Model):
    Animal_name = models.CharField(max_length=100)
    Animal_Weight = models.DecimalField(max_digits=5, decimal_places=2)
    Animal_Prize = models.DecimalField(max_digits=8, decimal_places=2)
    Animal_Farm = models.CharField(max_length=100, default='Unknown')
    Animal_description = models.TextField()
    Animal_image = models.ImageField(upload_to='animal_images', default='https://via.placeholder.com/150')

    def __str__(self):
        return self.Animal_name