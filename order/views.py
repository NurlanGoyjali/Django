from pyexpat.errors import messages

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.crypto import get_random_string

from home.models import UserProfile
from order.models import ShopCartForm, ShopCart, OrderForm, Order, OrderProduct
from product.models import Category, Product


@login_required(login_url='/login')
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkcart = ShopCart.objects.filter(product__id=id)

    if checkcart:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():

            if control == 1:
                data = ShopCart.objects.filter(product__id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:

                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        request.session['cart_items'] = ShopCart.objects.filter(user__id=current_user.id).count()
        return HttpResponseRedirect(url)

    else:
        if control == 1:
            data = ShopCart.objects.get(product__id=id)
            data.quantity += 1
            data.save()
        else:
            current_user = request.user
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user__id=current_user.id).count()
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def index(request):
    current_user = request.user
    category = Category.objects.all()
    cart = ShopCart.objects.all()
    scart = ShopCart.objects.filter(user__id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user__id=current_user.id).count()
    deneme = 123654
    total = 0
    for foo in scart:
        total = total + foo.amount

    context = {'category': category,
               'scart': scart,
               'deneme': deneme,
               'total': total,
               'cart': cart,
               }

    return render(request, 'shopcart.html', context)


@login_required(login_url='/login')
def productdeletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user__id=current_user.id).count()
    return HttpResponseRedirect('/shopcart')


@login_required(login_url='/login')
def orderproduct(request):

    current_user = request.user
    category = Category.objects.all()
    schopcart = ShopCart.objects.all().filter(user_id=current_user.id)
    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            # move Shopcart items to Order Products items
            schopcart = ShopCart.objects.filter(user_id=current_user.id)
            for rs in schopcart:
                detail = OrderProduct()

                detail.order_id = data.id  # Order Id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()
                # ***Reduce quantity of sold product from Amount of Product


            ShopCart.objects.filter(user_id=current_user.id).delete()  # Clear & Delete shopcart
            request.session['cart_items'] = 0

            return render(request, 'orderproduct.html', {'ordercode': ordercode, 'category': category})

        else:
            return HttpResponseRedirect('/order/orderproduct')

    else:
        form = OrderForm()
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {
                   'schopcart': schopcart,
                   'category': category,
                   'total': total,
                   'form': form,
                   'profile': profile,
                   }
        return render(request, 'order_form.html', context)


def orderdetail(request):

    return None