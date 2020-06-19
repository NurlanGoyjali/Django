from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='shopcart'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart '),
    path('deletefromcart/<int:id>', views.productdeletefromcart, name='productdeletefromcart '),
    path('orderproduct/', views.orderproduct, name='orderproduct'),

    # path('<int:idd>', views.index),

]
