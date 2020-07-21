from django.db import models

class User(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    PhoneNumber=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
