from django.db import models

# Create your models here.

class User(models.Model):
    id=models.IntegerField(primary_key=True , unique=True)
    FullName=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)