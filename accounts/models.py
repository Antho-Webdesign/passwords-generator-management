from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    rue = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
'''
'''
# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    rue = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=100, null=True)
    pass
'''