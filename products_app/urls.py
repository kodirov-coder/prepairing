from django.urls import path

from .views import index, products, basket_add, basket_remove

app_name = "products"

urlpatterns = [
    path("", index, name="main-page"),
    path("products", products, name="products"),
    path("category/<int:category_id>/", products, name="category"),
    path("basket/add/<int:product_id>/", basket_add, name="basket-add"),
    path("basket/remove/<int:basket_id>/", basket_remove, name="basket-remove"),
]
