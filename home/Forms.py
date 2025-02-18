from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100)


class SingUp(UserCreationForm):
    username = forms.CharField(max_length=30, label='username')
    email = forms.EmailField(max_length=100, label='email')
    first_name = forms.CharField(max_length=50, help_text='First Name', label='First Name :')
    last_name = forms.CharField(max_length=50, help_text='Last Name', label='Last Name :')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

