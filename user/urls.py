from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='user_profile '),
    path('update/', views.user_update, name='sing_up '),
    path('pass/', views.change_password, name='change_password '),
    path('userorders/', views.userorders, name='userorders '),
    path('orderdetail/<int:id>', views.orderdetail, name='orderdetail'),
    path('comments/', views.comments, name='comments '),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment '),
    # path('<int:idd>', views.index),

]
