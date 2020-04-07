from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index),

 # yuxardakının tam halı budu -> path('', views.results, name='results'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),

]