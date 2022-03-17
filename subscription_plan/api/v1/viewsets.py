from django.utils import timezone
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import PlanSerializer
from subscription_plan.models import Plan
from .serializers import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = [IsAuthenticated]
    queryset = Plan.objects.all()

    def create(self, request):
        """Creates a new Subscription Plan.
            Input Body:
                name: String
                description: String
                price: int
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'Pricing plan successfully added.'},
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTT_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieves Subscription Plan"""
        plan_instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(plan_instance)
        return Response({
            'data': serializer.data,
            'message': 'Your pricing plan retrieved.'},
            status=status.HTTP_200_OK)

    def update(self, request, pk=None,  *args, **kwargs):
        """Update the Subscription Plan
            Input Body:
                name: String
                description: String
                price: int
        """
        plan_instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(plan_instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializer = self.serializer_class(plan_instance)
            return Response({
                'data': serializer.data,
                'message': 'Pricing plan successfully updated.'},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTT_400_BAD_REQUEST)

     # Not allowed functions. Prevent unauthorized activity.
    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        plan_instance = get_object_or_404(self.queryset, pk=pk)
        plan_instance.delete()
        return Response({'message': 'Pricing plan successfully deleted.'}, status=status.HTTP_200_OK)
