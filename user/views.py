from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from order.models import Order, OrderProduct
from product.models import Category, Comment
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    idd = request.user.id
    profile = UserProfile.objects.get(user_id=idd)
    category = Category.objects.all()
    context = {
        'category': category,
        'profile': profile}
    return render(request, 'user_profile.html', context)




@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  # request.user is user data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'parola değişti')
            return HttpResponseRedirect('/login/')
        else:
            messages.error(request, 'parola işinde hata oluştu')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)

    return render(request, "change_pass.html", {'category': category , 'form': form})


def userorders(request):
    category = Category.objects.all()
    orderp = OrderProduct.objects.filter(user_id=request.user.id)

    context = {
        'category': category,
        'orderp': orderp,
    }

    return render(request, "orders.html", context)


def orderdetail(request,id):
    category = Category.objects.all()
    order = Order.objects.get(pk=id)

    context = {
        'category': category,
        'order': order,
    }

    return render(request, "orderdetail.html", context)

    return None


def comments(request):
    category = Category.objects.all()
    comment = Comment.objects.filter(user_id=request.user.id)
    context = {
        'comment': comment,
        'category': category,

    }
    return render(request,"comments.html",context)


def deletecomment(request, id):

    Comment.objects.filter(id=id, user_id=request.user.id).delete()
    messages.success(request, "Yorumunuz silindi")
    return HttpResponseRedirect('/user/comments')