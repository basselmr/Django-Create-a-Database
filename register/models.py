from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length = 255,unique=True)
    rating = models.IntegerField(default=5)

class Register(models.Model):
    userid = models.CharField(max_length = 255, unique=True)
    firstname=models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)