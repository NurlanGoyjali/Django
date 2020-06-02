"""deneme3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from home import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('home/', views.index , name='index'),
    path('index/', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact-us/', views.contact, name='contact-us'),
    path('category/<int:id>/<slug:slug>/', views.category_product, name='category_product'),
    path('product/<int:id>/', views.product_detail, name='category_product'),
    path('search/', views.search, name='search'),
    path('login/', views.log_in , name='login'),
    path('logout/', views.log_out, name='logout'),
    path('singup/', views.sing_up, name='singup'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
