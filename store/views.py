from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category

# Create your views here.
def index(request):
    products=None
    categories=Category.get_all_categories()
    category_id=request.GET.get('category')
    if category_id:
        products=Product.get_all_products_by_category_id(category_id)
    else:
        products=Product.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories
    return render(request,'index.html',data)
    # return render(request,"orders/order.html")

