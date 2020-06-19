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



    path(r'admin/', admin.site.urls),
    path(r'', views.index, name='index'),
    path(r'home/', views.index, name='index'),
    path(r'index/', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'contact-us/', views.contact, name='contact-us'),
    path(r'category/<int:id>/<slug:slug>/', views.category_product, name='category_product'),
    path(r'product/<int:id>/', views.product_detail, name='category_product'),
    path(r'search/', views.search, name='search'),
    path(r'login/', views.log_in, name='login'),
    path(r'logout/', views.log_out, name='logout'),
    path(r'contentdetail/<int:id>/', views.contentdetail, name='contentdetail'),
    path(r'menu/', views.menu, name='menu'),
    path(r'content/', views.content, name='content'),
    path(r'faq/', views.faq, name='faq'),
    path(r'404h/', views.error, name='404h'),
    path(r'singup/', views.sing_up, name='sing_up '),
    #path('singup/', views.sing_up, name='singup'),


    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    path(r'', include('home.urls')),
    path(r'product/', include('product.urls')),
    path(r'content/', include('content.urls')),
    path(r'user/', include('user.urls')),
    path(r'order/', include('order.urls')),
    path(r'shopcart/', include('order.urls')),

]
handler404 = 'deneme3.views.my_custom_page_not_found_view'
handler500 = 'deneme3.views.custom_error_view'
handler403 = 'deneme3.views.custom_permission_denied_view'
handler400 = 'deneme3.views.custom_bad_request_view'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
