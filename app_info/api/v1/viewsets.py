from rest_framework import authentication
from app_info.models import App
from .serializers import AppSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from app_info.models import App
from subscription.api.v1.serializers import SubscriptionSerializer
from subscription.api.v1.services import get_subscription_by_app_id, update_subscription_by_app_id
from .serializers import AppSerializer, AppWithSubscriptionDetailSerializer
from app_info.api.v1.services import get_app

class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = [IsAuthenticated]
    queryset = App.objects.all()
    def create(self, request):
        """
            Creates a new app with details.
            Input:
                name: String
                description: String
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({
                'data': serializer.data,
                'message': 'App info successfully added.'},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTT_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieves information about an app """
        app_instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(app_instance)
        return Response({
            'data': serializer.data,
            'message': 'Your app info retrieved.'},
            status=status.HTTP_200_OK)

    def update(self, request, pk=None,  *args, **kwargs):
        """Update the App info.
            Input:
                name: String
                description: String
        """
        app_instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(app_instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializer = self.serializer_class(app_instance)
            return Response({
                'data': serializer.data,
                'message': 'App info successfully updated.'},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTT_400_BAD_REQUEST)
     # Not allowed functions. Prevent unauthorized activity.

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        """Delet an app by id"""
        app_instance = get_object_or_404(self.queryset, pk=pk)
        app_instance.delete()
        return Response({'message': 'App successfully deleted.'}, status=status.HTTP_200_OK)


@api_view()
def get_subscription_by_appId(request, app_id):
    """
        Custom api endpoint to retrieve app with subscription
        Url param:
            app_id: int
    """
    app_instance = get_app(app_id)
    serializer = AppWithSubscriptionDetailSerializer(app_instance)
    return Response({
        'data': serializer.data,
        'message': 'Your app retrieved with subscription.'},
        status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_subscription_by_appId(request, app_id):
    """
        Update the subscription for an app.
        Url param:
            app_id: int
        Input body:
            plan: String
            is_active: String
    """
    plan_id = request.data["plan"]
    is_active = request.data["is_active"]
    app_instance = get_app(app_id)
    update_subscription_by_app_id(app_instance.id, plan_id, is_active)
    serializer = AppWithSubscriptionDetailSerializer(app_instance)
    return Response({
        'data': serializer.data,
        'message': 'App subscription successfully updated.'},
        status=status.HTTP_200_OK)
