from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profileIMG = models.ImageField(null=True, blank=True)