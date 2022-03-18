from rest_framework import authentication
from subscription.models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from subscription_plan.api.v1.services import get_subscription_plan
from subscription.models import Subscription
from .serializers import SubscriptionSerializer
from app_info.api.v1.services import get_app


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()

    def create(self, request):
        """Creates a subscription
            Input:
                app: int
                plan: int
                is_active: String
        """
        app = request.data['app']
        plan = request.data['plan']

        plan = get_subscription_plan(plan)
        app_instance = get_app(app)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(app=app_instance, plan=plan, user=request.user)
            return Response({
                'data': serializer.data,
                'message': 'Subscription successfully added.'},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTT_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieves a subscription"""
        app_instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(app_instance)
        return Response({
            'data': serializer.data,
            'message': 'Your Subscription retrieved.'},
            status=status.HTTP_200_OK)

    def update(self, request, pk=None,  *args, **kwargs):
        """ Update a subscription.
            Url param: subscription_id: int
            Input:
                app: int
                plan: int
                is_active: String
        """
        subscription_instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(
            subscription_instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializer = self.serializer_class(subscription_instance)
            return Response({
                'data': serializer.data,
                'message': 'Subscription successfully updated.'},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTT_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        app_instance = get_object_or_404(self.queryset, pk=pk)
        app_instance.delete()
        return Response({'message': 'Subscription successfully deleted.'}, status=status.HTTP_200_OK)
