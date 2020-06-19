from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from product.models import Comment, CommentForm


def index(request):

    return HttpResponse("Product Page")


@login_required(login_url='/login')
def add(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment()
            data.user_id = current_user.id
            data.product_id = id
            data.subject = request.user.username
            data.comment = form.cleaned_data['comment']
            #data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz Başarılı bir şekilde eklendi")
            #url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "Yorumunuz Eklenemedi :( ")
    return HttpResponseRedirect(url)
