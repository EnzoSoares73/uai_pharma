from django.shortcuts import render

def dashboard(request):
    context = {
    }
    return render(request, "authentication/dashboard.html", context)