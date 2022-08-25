from django.template import Library

register = Library()


@register.filter
def format_price(val):
    return f"R$ {val:.2f}".replace(".", ",")
