from rest_framework import authentication
from subscription.models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import viewsets


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subscription.objects.all()
