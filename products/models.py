from django.db import models
from django.contrib.auth.models import User

# Create your Products models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    prod_desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prod_image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name
        


# Create your User models here
class Cakeuser(models.Model):
    Cakeuser = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user')
    firstname = models.CharField("First Name", max_length=25)
    lastname = models.CharField("Last Name", max_length=25)
    address = models.CharField("Address line 1", max_length=25)
    city = models.CharField("City", max_length=25)
    state = models.CharField("State", max_length=25)
    zipcode = models.CharField("Zip Code", max_length=9)
    
    def __str__(self):
        return self.Cakeuser.firstname
        