from django.contrib import messages
from django.views import generic
from todo.forms.login import LoginForm

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm


class LoginFormView(generic.FormView):
    template_name = 'login_form.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, f"Vous êtes maintenant connecté en tant que {username}.")
        else:
            messages.error(self.request, "Nom d'utilisateur ou mot de passe invalide.")
        return super().form_valid(form)


def login_request(request):
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.info(self.request, f"Vous êtes maintenant connecté en tant que {username}.")
        else:
            messages.error(self.request, "Nom d'utilisateur ou mot de passe invalide.")
        return super().form_valid(form)


