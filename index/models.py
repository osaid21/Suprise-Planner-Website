from django.db import models

# Create your models here.

class gifts:
    name:str
    price:int
    img:str


class Customize(models.Model):
    ordername = models.CharField(max_length=30,null=True)
    orderdate = models.CharField(max_length=30,null=True)
    changes=models.TextField(max_length=500,null=True)
    phno=models.CharField(max_length=10,null=True)

    
    def __str__(self):
        return self.ordername

class Checkout(models.Model):
    date = models.CharField(max_length=30,null=True)
    time = models.CharField(max_length=30,null=True)

