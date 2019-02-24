from django import forms
from almacen.models import Products, Sales, Expenses
from almacen.choices import *

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'cod',
            'unitv',
            'amoutn',
            'total',
            'date',
        ]
        labels={
            'cod': 'Codigo',
            'unitv': 'Precio',
            'amoutn': 'Cantidad',
            'total': 'Total',
            'date': 'Fecha',
        }
        widgets={
            'cod': forms.TextInput(attrs={'class':'form-control'}),
            'unitv': forms.NumberInput(attrs={'class':'form-control'}),
            'amoutn': forms.NumberInput(attrs={'class':'form-control'}),
            'total': forms.NumberInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
        }


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = [
            'date',
            'cod',
            'unitv',
        ]
        labels={
            'date': 'Fecha',
            'cod': 'Codigo',
            'unitv': 'Valor Unitario',
        }
        widgets={
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'cod': forms.Select(attrs={'class':'form-control'}),
            'unitv': forms.NumberInput(attrs={'class':'form-control'}),
        }

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = [
            'description',
            'value',
            'date',
        ]
        labels={
            'description': 'Descripción',
            'value': 'Valor Unitario',
            'date': 'Fecha',
        }
        widgets={
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'value': forms.NumberInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
        }