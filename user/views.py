from django.shortcuts import render

# Create your views here.
from home.models import UserProfile
from product.models import Category


def index(request):
    idd = request.user.id
    profile = UserProfile.objects.get(user_id=idd)
    category = Category.objects.all()
    context = {
        'category': category,
        'profile': profile}
    return render(request, 'user_profile.html', context)
