from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class GenPass(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    site = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    passwords = models.CharField(max_length=300)

    def __str__(self):
        return self.site

