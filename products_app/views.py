from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    return render(request, "index.html")


def products(request):
    products = Product.objects.all()
    categorys = ProductCategory.objects.all()

    context = {
        "products": products,
        "categorys": categorys
    }
    return render(request, "products.html", context)