from django.db import models

    
    
class Signup(models.Model):
    name = models.CharField(max_length= 20)
    email = models.EmailField()
    password = models.CharField(max_length=10)



class Product(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2 )


    