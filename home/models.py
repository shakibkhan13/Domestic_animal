from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    # user = models.ForeignKey(User, on_Delete=models.SET_NULL , null=True ,blank=True)
    Animal_name = models.CharField(max_length=100)
    Animal_Weight = models.TextField()
    Animal_description = models.TextField()
    Animal_image = models.ImageField(upload_to="animal")
    Animal_Prize = models.TextField()
    Animal_Farm = models.TextField()
    Animal_view_count = models.IntegerField(default=1)
