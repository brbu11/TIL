from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=100, default='', unique=True)
    password = models.CharField(max_length=50, default='')


class Profile(models.Model):
    last_name = models.CharField(max_length=10, default='')
    first_name = models.CharField(max_length=20, default='')
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
