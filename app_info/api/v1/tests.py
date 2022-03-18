import json
from users.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from rest_framework import status
from app_info.models import App
from app_info.api.v1.serializers import AppSerializer


class AppInfoTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="kenmartey", email="ken@gmail.com", password="veryStrong123!")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def create_fake_data(self):
        data = {"name": "Some name",
                "description": "Some description", "user": 1}
        response = self.client.post("/api/v1/app/", data)
        return response

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))

    def test_create_app(self):
        data = {"name": "Some name",
                "description": "Some description", "user": 1}
        response = self.client.post("/api/v1/app/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_app(self):
        data = self.create_fake_data()
        response = self.client.get("/api/v1/app/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_app(self):
        data = self.create_fake_data()
        update_response = self.client.put(
            "/api/v1/app/3/", data.json()['data'])
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
