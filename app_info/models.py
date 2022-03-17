from django.conf import settings
from django.db import models


class App(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField()
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    date_modified = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="app_user",
    )


# Create your models here.
