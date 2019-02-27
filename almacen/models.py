from django.db import models
from django.urls import reverse
import datetime
from almacen.choices import *

# Create your models here.

class Products(models.Model):

    """ Categorias para clasificar los productos """
    cod = models.CharField(max_length=4)
    unitv = models.PositiveIntegerField( "unitv")
    amoutn = models.PositiveIntegerField( "amout")
    total = models.PositiveIntegerField( )
    date = models.DateField( "date", default=datetime.date.today)

    def __str__(self):
        return self.cod
    def get_absolute_url(self):
        return reverse('products-list')
    class Meta:
        ordering=["-id"]

class Sales(models.Model):

    """ Categorias para clasificar las ventas """
    date = models.DateField( "date", default=datetime.date.today)
    cod = models.CharField(max_length=4, choices=CODIGOS_CHOICES)        
    unitv = models.PositiveIntegerField( )

    def __str__(self):
        return self.cod 
    def get_absolute_url(self):
        return reverse('sales-list')
    class Meta:
        ordering=["-id"]

class Expenses(models.Model):

    """ Categorias para clasificar los gastos """
    description = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    date = models.DateField( "date", default=datetime.date.today)
    
    def __str__(self):
        return self.description
    def get_absolute_url(self):
        return reverse('expenses-list')
    class Meta:
        ordering=["-id"]