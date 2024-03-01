from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    print(len(products))
    return render(request, 'product_list.html', {'products': products})

