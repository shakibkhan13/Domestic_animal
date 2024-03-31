from django.db import models
from django.contrib.auth.models import AbstractUser

class Animal(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_animals')
    Animal_name = models.CharField(max_length=100)
    Animal_Weight = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Prize = models.DecimalField(max_digits=10, decimal_places=2) 
    Animal_Farm = models.CharField(max_length=100, default='Unknown')
    Animal_color = models.CharField(max_length=100, default='Unknown')
    Animal_description = models.TextField()
    Animal_image = models.ImageField(upload_to='animal_images', default='')

    def __str__(self):
        return self.Animal_name

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='+'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='+'
    )

    def __str__(self):
        return self.username
