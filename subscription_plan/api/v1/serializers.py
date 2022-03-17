from rest_framework import serializers
from subscription_plan.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"

    def validate(self, data):
        """
            Object level validation on Subscription Plans
        """
        name = data.get('name', None)
        price = data.get('price', None)
        description = data.get('description', None)

        if name is None or name == "":
            raise serializers.ValidationError(
                'Add a price name')

        if description is None or description == "":
            raise serializers.ValidationError(
                'Add some description to the plan')

        if price is None or price == "":
            raise serializers.ValidationError(
                'Input price associated with the plan')
        return data

    def create(self, validated_data):
        plan = Plan.objects.create(
            **validated_data
        )

        return plan

    def update(self, instance, validated_data):
        """ Only Fields users can change or edit.
            [name, description, price]
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.price = validated_data.get(
            'price', instance.price)
        instance.save()
        return instance
