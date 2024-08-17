from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def get_total_price(self):
        return self.product.price * self.quantity

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    
    def get_total_amount(self):
        return sum(item.get_total_price() for item in self.items.all())