from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField(unique = True)
    date_subscribed = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.email



# model for your own login
class Rotate(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    
    def __str__(self):
        return self.username