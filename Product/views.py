from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from . import models


class ListProducts(ListView):
    """List Product View"""

    model = models.Product
    template_name = "product/list.html"
    paginate_by = 3
    context_object_name = "products"
    # TODO: Change it after testing the pagination feature


class ProductDetails(DetailView):
    """Product Details View"""

    model = models.Product
    template_name = "product/detail.html"
    context_object_name = "product"
    slug_url_kwarg = "slug"


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
