from django.conf import settings
from django.db import models
from django.urls import reverse

from shop. models import Product, Category
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'
    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return '{}'.format(self.product)

    def get_absolute_url(self):
        print("here1")
        path = reverse('shop:productCategoryDetails', args=[self.product.category.slug, self.product.slug])
        print("here2")

        return '{}{}'.format(settings.BASE_URL, path)


