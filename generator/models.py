from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


# Create your models here.
class GenPass(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    site = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    passwords = models.CharField(max_length=300)

    def __str__(self):
        return self.site

    class Meta:
        verbose_name = 'genpass'
        verbose_name_plural = 'liste mots de passe'
        ordering = ['user']



