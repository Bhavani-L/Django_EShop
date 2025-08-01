from django.contrib import admin
from .models.product import Product
from .models.category import Category

class adminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class adminCategory(admin.ModelAdmin):
    list_display=['name']


# Register your models here.
admin.site.register(Product,adminProduct)
admin.site.register(Category,adminCategory)