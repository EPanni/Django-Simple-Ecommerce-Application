from cgi import print_exception
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import User


class Order(models.Model):
    """Order Model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ("A", "Approved"),
            ("C", "Created"),
            ("R", "Reproved"),
            ("P", "Pendent"),
            ("S", "Sent"),
            ("F", "Finishes"),
        ),
    )

    def __str__(self):
        return f" Order n. {self.pk}"


class OrderItem(models.Model):
    """Item Model"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    producti_id = models.PositiveBigIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    # TODO: Verify if it is really necessary to have the price promo here
    price_promo = models.FloatField(default=0)
    amount = models.PositiveIntegerField()
    image = models.CharField(
        max_length=2000
    )  # This field considers the current image when the product is bought

    def __str__(self):
        return f" Order's item n. {self.order}"
