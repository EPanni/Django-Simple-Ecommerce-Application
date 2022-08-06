from django.contrib import admin
from . import models


class OrderItemInLine(admin.TabularInline):
    model = models.OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]


admin.site.register(models.Order),
admin.site.register(models.OrderItem)
