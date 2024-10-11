from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import Group
from .forms import ProductForm, OrderForm
from .models import Product, Order


def main_index(request: HttpRequest):
    databases = [
        ('Mysql', 10),
        ('Postgres', 20),
        ('Mssql', 30),
    ]
    
    webservers = [
        ('nginx', 400),
        ('apache', 120),
        ('caddy', 80),
    ]
    
    username = 'user'
    plus_count = 50
    
    context = {
        "databases": databases,
        "webservers": webservers,
        "username": username,
        "plus_count": plus_count
    }
    return render(request, 'shopapp/shop.html', context=context)

def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("shopapp:products_list")
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, 'shopapp/create-product.html', context=context)

def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def create_order(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("shopapp:orders_list")
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        "form": form,
    }
    return render(request, 'shopapp/create-order.html', context=context)

def main_shop_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'shopapp/mainshop.html')