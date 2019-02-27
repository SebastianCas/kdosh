from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from rest_framework import generics
from almacen.models import Products, Sales, Expenses
from django.views.generic import ListView, DetailView, TemplateView 
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from almacen.forms import ProductsForm, SalesForm, ExpensesForm
from django.template import RequestContext
from django.contrib import messages

# Create your views here.
def first_view(request):
    return render(request, 'bienvenido.html')

#lista
def ProductsListView(request):
    return render(request, 'almacen/products_form.html')

class ProductsDetailView(DetailView):
    model = Products

class ExpensesListView(ListView):
    model=Expenses
    template_name = 'almacen/expenses_list.html'
    paginate_by=4
class ExpensesDetailView(DetailView):
    model = Expenses

def inventory(request):
    product=Products.objects.all()
    sales=Sales.objects.all()
    context={'products':product, 'sales':sales}
    return render(request, 'almacen/inventory_list.html', context)

#create
class ProductsCreate(CreateView):
    model = Products
    template_name = "almacen/products_form.html"
    form_class = ProductsForm
    success_url = reverse_lazy('products-create')

class SalesCreate(CreateView):
    model = Sales
    template_name = "almacen/sales_form.html"
    form_class = SalesForm 
    success_url = reverse_lazy('sales-create')

class ExpensesCreate(CreateView):
    model = Expenses
    template_name = "almacen/expenses_form.html"
    form_class = ExpensesForm

#Delete
class ExpensesDelete(DeleteView):
    model = Expenses
    success_url = reverse_lazy('expenses-list')

class ProductsDelete(DeleteView):
    model = Products
    success_url = reverse_lazy('inventory-list')

class SalesDelete(DeleteView):
    model = Sales
    success_url = reverse_lazy('inventory-list')

#update
class ProductsUpdate(UpdateView):
    model = Products
    template_name= "almacen/products_form.html"
    form_class = ProductsForm
    success_url = reverse_lazy('inventory-list')

class SalesUpdate(UpdateView):
    model = Sales
    template_name= "almacen/sales_form.html"
    form_class = SalesForm
    success_url = reverse_lazy('inventory-list')