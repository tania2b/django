from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30,  widget=forms.TextInput(attrs={'class': 'input',  'placeholder': 'Username'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'input',  'placeholder': 'Password'}))
