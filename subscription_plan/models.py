from django.conf import settings
from django.db import models


class Plan(models.Model):
    "Generated Model"
    name = models.TextField(
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )
    price = models.IntegerField(
        blank=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )
    date_modified = models.DateTimeField(
        auto_now=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="plan_user",
        blank=True,
    )


# Create your models here.
