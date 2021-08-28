from django.urls import path, include
from . import views

app_name = "authentication"
urlpatterns = [
    path("accounts", include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
]
