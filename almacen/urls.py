from django.shortcuts import render
from django.urls import path
from almacen import views 
from django.contrib.auth.decorators import login_required

# Create your views here.
urlpatterns = [
    path('', (views.first_view), name='base'),

    path('products/', (views.ProductsListView), name='products-list'),
    path('products/<int:pk>/detail/', (views.ProductsDetailView.as_view()), name='products-detail'),

    path('inventory/', (views.inventory), name='inventory-list'),

    path('expenses/', (views.ExpensesListView.as_view()), name='expenses-list'),
    path('expenses/<int:pk>/detail/', (views.ExpensesDetailView.as_view()), name='expenses-detail'),

    #Create
    path('products/create/', (views.ProductsCreate.as_view()), name='products-create'),
    path('sales/create/', (views.SalesCreate.as_view()), name='sales-create'),
    path('expenses/create/', (views.ExpensesCreate.as_view()), name='expenses-create'),

    #Delete
    path('expenses/<int:pk>/delete/', (views.ExpensesDelete.as_view()), name='expenses-delete'),
    path('products/<int:pk>/delete/', (views.ProductsDelete.as_view()), name='products-delete'),

    #update
    path('products/<int:pk>/update/', (views.ProductsUpdate.as_view()), name='products-update'),
    
    #path('about/', (views.ProductsListView.as_view()), name='about'),
]
