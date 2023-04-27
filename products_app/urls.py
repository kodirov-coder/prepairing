from django.urls import path

from .views import index, products

app_name = "products"

urlpatterns = [
    path("", index, name="main-page"),
    path("products", products, name="products")
]
