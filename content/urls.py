from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='user_profile '),

    # path('<int:idd>', views.index),

]
