from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.urls import reverse_lazy
from rest_framework import generics
from almacen.models import Products, Sales, Expenses
from django.views.generic import ListView, DetailView, TemplateView 
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from almacen.forms import ProductsForm, SalesForm, ExpensesForm
from django.template import RequestContext
from django.core.paginator import Paginator
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
    product_list=Products.objects.all().order_by("-id")
    sales_list=Sales.objects.all().order_by("-id")

    paginator = Paginator(product_list, 1)
    paginator2 = Paginator(sales_list, 1)

    page = request.GET.get('page')
    product = paginator.get_page(page)
    sales = paginator2.get_page(page)

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

class Buscar(TemplateView):
    template_name = "almacen/buscar.html"
    def post(self, request, *args, **kwargs):
        buscar=request.POST['cod']
        buscar2=request.POST['date']

        if buscar2:
            if buscar:
                product_list=Products.objects.filter(cod__contains=buscar,date__contains=buscar2)
                sales_list=Sales.objects.filter(cod__contains=buscar,date__contains=buscar2)

                paginator = Paginator(product_list, 1)
                paginator2 = Paginator(sales_list, 1)

                page = request.GET.get('page')
                ventas = paginator2.get_page(page)
                producto = paginator2.get_page(page)

                context={'producto':producto, 'ventas':ventas}
                return render(request, "almacen/buscar.html", context)
            else:
                if buscar2:
                    product_list=Products.objects.filter(date__contains=buscar2)
                    sales_list=Sales.objects.filter(date__contains=buscar2)
                    
                    paginator = Paginator(product_list, 1)
                    paginator2 = Paginator(sales_list, 1)

                    page = request.GET.get('page')
                    ventas = paginator2.get_page(page)
                    producto = paginator2.get_page(page)

                    context={'producto':producto, 'ventas':ventas}
                    return render(request, "almacen/buscar.html", context)
                
                elif buscar:
                    product_list=Products.objects.filter(cod__contains=buscar)
                    sales_list=Sales.objects.filter(cod__contains=buscar)

                    paginator = Paginator(product_list, 1)
                    paginator2 = Paginator(sales_list, 1)

                    page = request.GET.get('page')
                    ventas = paginator2.get_page(page)
                    producto = paginator2.get_page(page)

                    context={'producto':producto, 'ventas':ventas}
                    return render(request, "almacen/buscar.html", context)
        elif buscar:
            product_list=Products.objects.filter(cod__contains=buscar)
            sales_list=Sales.objects.filter(cod__contains=buscar)

            paginator = Paginator(product_list, 1)
            paginator2 = Paginator(sales_list, 1)

            page = request.GET.get('page')
            ventas = paginator2.get_page(page)
            producto = paginator2.get_page(page)

            context={'producto':producto, 'ventas':ventas}
            return render(request, "almacen/buscar.html", context)
        
        else:
            return render(request, "almacen/buscar.html")
        