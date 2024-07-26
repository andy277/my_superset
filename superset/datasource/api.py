import logging
from flask_appbuilder.api import expose, protect, safe, BaseApi
from superset.views.base_api import BaseSupersetApi, statsd_metrics
from superset.superset_typing import FlaskResponse

logger = logging.getLogger(__name__)


class DatasourceRestApi(BaseSupersetApi):
    route_base = "/datasource"

    @expose("/greeting")
    def greet(self) -> FlaskResponse:
        """Send a greeting
            ---
            get:
              responses:
                200:
                  description: Greet the user
                  content:
                    application/json:
                      schema:
                        type: object
                        properties:
                          message:
                            type: string
            """
        return self.response(200, message="Hello")
