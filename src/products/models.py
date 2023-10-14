from django.db import models

from app.models import TimestampedModel


class Category(TimestampedModel):
    name = models.CharField(max_length=255)


class Product(TimestampedModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
