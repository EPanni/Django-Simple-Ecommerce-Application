from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class Create(ListView):
    """Create View"""

    def get(self, *args, **kwargs):
        return HttpResponse("Create")


class Update(ListView):
    """Update View"""

    def get(self, *args, **kwargs):
        return HttpResponse("Update")


class Login(ListView):
    """Login View"""

    def get(self, *args, **kwargs):
        return HttpResponse("Login")


class Logout(ListView):
    """Logout View"""

    def get(self, *args, **kwargs):
        return HttpResponse("Logout")
