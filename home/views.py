from typing import re

from django.http import HttpResponse
from django.shortcuts import render
from product.models import Product, Category

# Create your views here.

def index(request):
    prod_data = Product.objects.all()[:3]
    cate_data = Category.objects.all()[:4]
    feat_data = Product.objects.all()[:6]
    context = {'prod_data': prod_data, 'cate_data':cate_data,'feat_data':feat_data}

    return render(request, 'index.html', context)

def about(request):
    setting = Product.objects.get(pk=1)

    return render(request ,'about.html')

def contact(req):
    return render(req,'contact-us.html')
