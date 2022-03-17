from django.conf import settings
from django.db import models


class Subscription(models.Model):
    "Generated Model"
    app = models.ForeignKey(
        "app_info.App",
        on_delete=models.CASCADE,
        related_name="subscription_app",
    )
    plan = models.ForeignKey(
        "subscription_plan.Plan",
        on_delete=models.CASCADE,
        related_name="subscription_plan",
    )
    is_active = models.BooleanField()
    start_date = models.DateTimeField(
        auto_now_add=True,
    )
    date_modified = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscription_user",
        blank=True
    )


# Create your models here.
