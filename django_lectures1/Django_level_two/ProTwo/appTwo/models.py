from django.db import models
# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email=models.EmailField(max_length=264,unique=True)
