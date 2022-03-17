from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AppViewSet,  \
get_subscription_by_appId, update_subscription_by_appId

router = DefaultRouter()
router.register("app", AppViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("generatemodels/subscription/<int:app_id>",
         get_subscription_by_appId, name="get-subscription-by-app-id"),
    path("generatemodels/subscription/<int:app_id>/",
         update_subscription_by_appId, name="update-subscription-by-app-id")
]
