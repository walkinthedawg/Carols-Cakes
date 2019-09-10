from django.db import models
from django.contrib.auth.models import User

# Create your Products models here.
class Product(models.Model):
    name = models.CharField(max_length=300, default='')
    prod_desc = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prod_image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.name