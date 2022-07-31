from distutils.command.upload import upload
from pickletools import optimize
from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.template import Origin

# Create your models here.
MAX_IMAGE_SIZE = 800


class Product(models.Model):
    """Model for Products"""

    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    description = models.TextField()
    # TODO: blank equals true only for testing. Remove it later
    image = models.ImageField(upload_to="products_img/%Y/%m", blank=True, null=True)
    slug = models.SlugField(unique=True)
    price_market = models.FloatField()
    price_promo = models.FloatField(default=0)
    prod_type = models.CharField(
        default="V",
        max_length=1,
        choices=(
            ("V", "Variation"),
            ("S", "Simple"),
        ),
    )

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def resize_image(image, new_width=800):
        """Resizes the image"""
        image_abs_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pil = Image.open(image_abs_path)
        original_width, original_height = image_pil.size
        if original_width > new_width:
            new_height = round(new_width * (original_height / original_width))
            new_image = image_pil.resize((new_width, new_height), Image.LANCZOS)
            new_image.save(image_abs_path, optimize=True, quality=50)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image(self.image, MAX_IMAGE_SIZE)


class Variation(models.Model):
    """Variation Models"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    price_promo = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name or self.product.name
