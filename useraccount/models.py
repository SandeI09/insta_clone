from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class User(AbstractUser):
    contact = models.CharField(max_length=255, blank=True, default="")
    address = models.CharField(max_length=255, blank=True, default="")
    profile_picture = models.ImageField(upload_to="profile_picture/",blank=True, null=True)

    



