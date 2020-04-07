from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    test = "product dan gelenler"
    context = {'text': test}
    return render(request,'index.html', context)
