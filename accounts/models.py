from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    foto= models.ImageField(upload_to='user_photos/', null=True, blank=True)
    ROLE_CHOICES = [
        ('client', 'Cliente'),
        ('translator', 'Traductor'),
    ]
    SEXE=[
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexe=models.CharField(max_length=1, choices=SEXE, default='M')
    pais=models.CharField(max_length=50, blank=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
