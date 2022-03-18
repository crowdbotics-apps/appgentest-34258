import json
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from rest_framework import status
from subscription_plan.models import Plan
from app_info.models import App
from subscription.models import Subscription


class AppInfoTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="kenmartey", email="ken@gmail.com", password="veryStrong123!")
        self.plan = Plan.objects.create(
            name="Free", description="Some description", price=0, user=self.user)
        self.app = App.objects.create(
            name="Name", description="something", user=self.user)
        self.subscription = Subscription.objects.create(
            app=self.app, plan=self.plan, is_active=True, user=self.user)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))

    def test_create_subscription(self):
        data = {"app": 1,
                "plan": 1, "is_active": True}
        response = self.client.post("/api/v1/subscription/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_subscription(self):
        response = self.client.get("/api/v1/subscription/3/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
