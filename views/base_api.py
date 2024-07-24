import logging
from typing import Any, Callable
from flask_appbuilder.api import BaseApi

logger = logging.getLogger(__name__)


class BaseSupersetApiMixin:
    csrf_exempt = False


class BaseSupersetApi(BaseSupersetApiMixin, BaseApi):
    ...


def statsd_metrics(f: Callable[..., Any]) -> Callable[..., Any]:
    """
    Handle sending all statsd metrics from the REST API
    """

