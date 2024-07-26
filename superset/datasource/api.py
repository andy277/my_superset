import logging
from flask_appbuilder.api import expose, protect, safe, BaseApi
from superset.views.base_api import BaseSupersetApi, statsd_metrics
from superset.superset_typing import FlaskResponse
from typing import Dict

logger = logging.getLogger(__name__)


class DatasourceRestApi(BaseSupersetApi):
    route_base = "/datasource"

    @expose("/greetings")
    def greet(self) -> FlaskResponse:
        return self.response(200, message="Hello world.")
