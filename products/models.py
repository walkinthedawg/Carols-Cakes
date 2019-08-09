from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    prod_desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prod_image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=15, default='')
    cat_desc = models.TextField()
    cat_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name