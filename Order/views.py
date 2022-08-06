from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


class Pay(ListView):
    """Pay View"""

    def get(self, *args, **kwargs):
        return HttpResponse("Pay")


class FinishOrder(ListView):
    """Finish Order View"""

    def get(self, *args, **kwargs):
        return HttpResponse("FinishOrder")


class Detail(ListView):
    """Detail view"""

    def get(self, *args, **kwargs):
        return HttpResponse("Detail")
