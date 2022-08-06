"""Order URLS"""
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("pay/", views.Pay.as_view(), name="pay"),
    path("finishorder/", views.FinishOrder.as_view(), name="finishorder"),
    path("detail/", views.Detail.as_view(), name="details"),
]
