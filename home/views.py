from django.contrib import messages
from typing import re

import json

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.Forms import SearchForm, SingUp
from home.models import UserProfile
from product.models import Product, Category, Images, Comment


# Create your views here.

def index(request):
    prod_data = Product.objects.all()[:3]
    cate_data = Category.objects.all()[:6]
    feat_data = Product.objects.all().order_by('?')[:6]
    category = Category.objects.all()
    dayproduct = Product.objects.all()[:3]
    lastproduct = Product.objects.all().order_by('?')[:3]
    productforu = Product.objects.all().order_by('?')[:3]

    sliderdata=Product.objects.all().order_by('?')[:3]
    context = {'prod_data': prod_data,
               'cate_data':cate_data,
               'feat_data':feat_data,
               'category': category,
               'sliderdata':sliderdata,
               'dayproduct':dayproduct,
               'lastproduct':lastproduct,
               'productforu':productforu
               }

    return render(request, 'index.html', context)


def about(request):
    category = Category.objects.all()
    setting = Product.objects.get(pk=1)
    context = {'category': category}

    return render(request ,'about.html',context)


def contact(req):

    category = Category.objects.all()
    context = {'category': category}
    return render(req,'contact-us.html',context)


def category_product(request, id, slug):
    feat_data=Product.objects.filter(category_id=id)
    category = Category.objects.all()
    productforu = Product.objects.all().order_by('?')[:3]
    context = {
        'slug':slug,
        'feat_data': feat_data,
        'category': category,
        'productforu': productforu,
    }

    return render(request, 'show_products.html', context)


def product_detail(request, id):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {
        'comments': comments,
        'category': category,
        'product': product,
        'images': images,
    }

    return render(request, 'product_detail.html', context)


def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            product = Product.objects.filter(title__icontains=query)
            context = {
                'category': category,
                'product': product,
            }
            return render(request,'product_search.html',context)
    return HttpResponseRedirect('/')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Bilgilerinizi Doğrulayın ")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')





def sing_up(request):
    if request.method == 'POST':
        form = SingUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'images/users/user.png'
            data.save()
            messages.success(request, 'hoş geldin')
            return HttpResponseRedirect('/')

    form = SingUp()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'singup.html', context)


