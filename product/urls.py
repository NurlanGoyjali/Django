from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index),
    path('add/<int:id>', views.add, name='add'),


]