from django.db import models

# Create your models here.

class Book(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Image = models.CharField(max_length=1000) # image URL