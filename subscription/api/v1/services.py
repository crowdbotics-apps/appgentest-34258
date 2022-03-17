
import logging
from pydoc import plain
from rest_framework import status
from rest_framework.exceptions import APIException
from subscription_plan.api.v1.services import get_subscription_plan
from subscription.models import Subscription

logger = logging.getLogger(__name__)


class NotFoundError(APIException):
    status_code = 404
    default_detail = 'Data not found'


def get_subscription_by_app_id(id):
    logger.info("Querying for Subscription with app id {id}")
    try:
        return Subscription.objects.get(app__id=id)
    except Subscription.DoesNotExist:
        logger.exception(
            {
                "message": f"Subscription with app id {id} does not exist",
            }
        )
        raise NotFoundError


def update_subscription_by_app_id(app_id, plan, is_active):
    logger.info("Update for Subscription with app id {id}")
    subscription = get_subscription_by_app_id(app_id)
    plan = get_subscription_plan(plan)
    subscription.plan = plan
    subscription.is_active = is_active
    subscription.save()
    return subscription
    