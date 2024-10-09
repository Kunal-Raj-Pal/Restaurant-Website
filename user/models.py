from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    menu = models.CharField(max_length=50)

    def __str__(self):
        return self.menu
    