
import logging
from rest_framework import status
from rest_framework.exceptions import APIException
from subscription_plan.models import Plan

logger = logging.getLogger(__name__)


class NotFoundError(APIException):
    status_code = 404
    default_detail = 'Data not found'


def get_subscription_plan(id):
    logger.info("Querying for plan with id {id}")
    try:
        return Plan.objects.get(id=id)
    except Plan.DoesNotExist:
        logger.exception(
            {
                "message": f"plan with id {id} does not exist",
            }
        )
        raise NotFoundError
