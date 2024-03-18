from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    Animal_name = models.CharField(max_length=100)
    Animal_Weight = models.CharField(max_length=100)
    Animal_description = models.TextField()
    Animal_image = models.ImageField(upload_to="animal")
    Animal_Prize = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    Animal_Farm = models.TextField(default='')
    Animal_view_count = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
