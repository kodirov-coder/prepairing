from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket


def index(request):
    return render(request, "index.html")


def products(request):
    products = Product.objects.all()
    category = ProductCategory.objects.all()

    context = {
        "products": products,
        "categorys": category
    }
    return render(request, "products.html", context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])