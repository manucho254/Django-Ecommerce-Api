from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class MyUser(AbstractBaseUser):
    phone = models.CharField(max_length=40, unique=True)

    USERNAME_FIELD = 'phone'