from rest_framework import serializers
from subscription.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

    def validate(self, data):
        """
            Object level validation on Subscription
        """
        is_active = data.get('is_active')
        if is_active is None or is_active == "":
            raise serializers.ValidationError(
                'is_active on subscription cannot be empty!')
        return data

    def create(self, validated_data):
        subscription = Subscription.objects.create(
            **validated_data
        )
        return subscription

    def update(self, instance, validated_data):
        """Only Fields users can change or edit.
            [app, is_active]
        """
        instance.app = validated_data.get(
            'app', instance.app)
        instance.plan = validated_data.get(
            'plan', instance.plan)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.save()
        return instance