from django.shortcuts import render
from . import models

# Create your views here.

def products(request):
    products = models.Product.objects.all()
    return render(request, 'products/products.html', {'products': products})
def product(request, id):
    product = models.Product.objects.get(id=id)
    return render(request, 'products/product.html', {'product': product})