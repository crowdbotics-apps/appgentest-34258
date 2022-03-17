
import logging
from rest_framework import status
from rest_framework.exceptions import APIException
from app_info.models import App

logger = logging.getLogger(__name__)


class NotFoundError(APIException):
    status_code = 404
    default_detail = 'Data not found'


def get_app(id):
    logger.info("Querying for app with id {id}")
    try:
        app = App.objects.get(id=id)
        return app
    except App.DoesNotExist:
        logger.exception(
            {
                "message": f"App with id {id} does not exist",
            }
        )
        raise NotFoundError
