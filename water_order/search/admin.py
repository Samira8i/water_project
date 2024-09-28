from django.contrib import admin

# Register your models here.
# orders/admin.py или search/admin.py
from django.contrib import admin
from .models import Product

admin.site.register(Product)
