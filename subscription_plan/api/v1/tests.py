import json
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from rest_framework import status


class AppInfoTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="kenmartey", email="ken@gmail.com", password="veryStrong123!")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.create_fake_data()

    def create_fake_data(self):
        data = {"name": "Some name",
                "description": "Some description", "price": 0}
        response = self.client.post("/api/v1/plan/", data)
        return response

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + str(self.token))

    def test_create_plan(self):
        data = {"name": "Some name",
                "description": "Some description", "price": 0, "user": 1}
        response = self.client.post("/api/v1/plan/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_plan(self):
        response = self.client.get("/api/v1/plan/3/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_plan(self):
        data = self.create_fake_data()
        update_response = self.client.put(
            "/api/v1/plan/5/", data.json()['data'])
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
