from django.conf import settings
from django.db import models


class Plan(models.Model):
    "Generated Model"
    tier = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    date_modified = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="plan_user",
    )


# Create your models here.
