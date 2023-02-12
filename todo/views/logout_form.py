from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class LogoutFormView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Vous avez été déconnecté avec succès.")
        return redirect("index")
