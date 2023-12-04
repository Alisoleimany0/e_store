from django.contrib import admin
from .models import Category, Order, Product, OrderItem, Cart
# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)