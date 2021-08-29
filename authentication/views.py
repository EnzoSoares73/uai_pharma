import logging
import os

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.urls import reverse

from authentication.forms import UserForm


def dashboard(request):
    context = {}
    return render(request, "authentication/dashboard.html", context)

def register(request):
    if request.method == "GET":
        context = {
            "form": UserForm
        }
        return render(request, "authentication/register.html", context)
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(make_password(form.cleaned_data['password']))
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        context = {
            "form": UserForm,
            "errors": form.errors
        }
        return render(request, "authentication/register.html", context)