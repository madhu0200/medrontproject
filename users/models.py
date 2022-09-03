from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
     # For now we do nothinng
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.username


class mobiles(models.Model):
    picture=models.FileField(upload_to='media/')
    name=models.CharField(max_length=25)
    brand=models.CharField(max_length=25)
    color=models.CharField(max_length=20)
    ram=models.IntegerField()
    rom=models.IntegerField()

class otp(models.Model):

        username=models.CharField(max_length=25)
        otps=models.IntegerField()

        def __str__(self):
            return self.username


