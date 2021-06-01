from django.db import models

# Create your models here.
class register(models.Model):
    Name=models.CharField(max_length=255)
    phonenumber=models.IntegerField()
    donatecount=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
