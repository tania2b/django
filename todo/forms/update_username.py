from django import forms
from django.contrib.auth.models import User


class UpdateUsernameForm(forms.Form):
    username = forms.CharField(label="Username", min_length=5, max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'input',  'placeholder': 'Username'})
                               )