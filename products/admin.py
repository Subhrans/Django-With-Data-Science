from django.contrib import admin
from products.models import Product,Purchase
# Register your models here.

admin.site.register(Product)
admin.site.register(Purchase)
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name','']