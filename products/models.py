from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Product(models.Model):
    prod_name = models.CharField(max_length=254, default='')
    prod_desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prod_image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=15, default='')
    cat_desc = models.TextField()
    cat_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.prod_name