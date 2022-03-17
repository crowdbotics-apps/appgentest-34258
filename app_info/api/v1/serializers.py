from rest_framework import serializers
from app_info.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"
