from django.contrib import admin
from . import models


class VariationInLine(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description", "format_price", "format_promo_price"]
    inlines = [VariationInLine]


# Register your models here.
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation)
