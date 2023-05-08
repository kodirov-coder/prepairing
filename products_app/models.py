from django.db import models

from users_app.models import Users

class ProductCategory(models.Model):
    name = models.CharField(max_length=125)
    descriptions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to="product-image")
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} --> {self.name}"


class BasketsQuerySet(models.QuerySet):
    def get_total_quantity(self):
        return sum(basket.quantity for basket in self)

    def get_total_price(self):
        return sum(basket.get_price() for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    creater_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketsQuerySet.as_manager()

    def __str__(self):
        return f"{self.user.username} uchun savatcha | Mahsulot: {self.product.name}, {self.quantity} dona"
    
    def get_price(self):
        return self.product.price*self.quantity