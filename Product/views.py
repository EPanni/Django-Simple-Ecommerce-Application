from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models


class ListProducts(ListView):
    """List Product View"""

    model = models.Product
    template_name = "product/list.html"
    context_object_name: "products"


class ProductDetails(ListView):
    """Product Details View"""

    def get(self, *args, **kwargs):
        return HttpResponse("ProductDetails")


class AddToCart(ListView):
    """Add To Cart View"""

    def get(self, *args, **kwargs):
        return HttpResponse("AddToCart")


class RemoveFromCart(ListView):
    """Remove From Cart View"""

    def get(self, *args, **kwargs):
        return HttpResponse("RemoveFromCart")


class Cart(ListView):
    """List Product View"""

    def get(self, *args, **kwargs):
        return HttpResponse("Cart")


class Finalize(ListView):
    """List Product View"""

    def get(self, *args, **kwargs):
        return HttpResponse("Finalize")
