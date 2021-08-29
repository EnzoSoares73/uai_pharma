from django.contrib import messages
from django.contrib.auth import login
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
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            messages.error(request, 'Email já utilizado')