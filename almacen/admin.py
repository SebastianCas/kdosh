from django.contrib import admin
from almacen.models import Products, Sales, Expenses

# Register your models here.
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(Expenses)
