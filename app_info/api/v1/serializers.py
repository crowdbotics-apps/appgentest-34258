from rest_framework import serializers
from app_info.models import App
from subscription.api.v1.serializers import SubscriptionSerializer

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"

        extra_kwargs = {'user': {'read_only': True}}

    def validate(self, data):
        """
            Object level validation on generate App Model
        """
        description = data.get('description', None)

        if description is None:
            raise serializers.ValidationError(
                'Atleast provide a brief description of your app.')
        return data

    def create(self, validated_data):
        generatedModel = App.objects.create(
            **validated_data
        )

        return generatedModel

    def update(self, instance, validated_data):
        """Only Fields users can change or edit.
            [name, description]
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance


class AppWithSubscriptionDetailSerializer(serializers.ModelSerializer):
    """
        A custom serializer to show subcription on an app.
    """
    subscription_app = SubscriptionSerializer(
        many=True)

    class Meta:
        model = App
        fields = ["id", "name", "description", "subscription_app"]
