import logging
from flask_appbuilder.api import expose, protect, safe
from superset.views.base_api import BaseSupersetApi, statsd_metrics
from superset.superset_typing import FlaskResponse

logger = logging.getLogger(__name__)


class DatasourceRestApi(BaseSupersetApi):
    allow_browser_login = True
    class_permission_name = "Datasource"
    resource_name = "datasource"
    openapi_spec_tag = "Datasources"

    @expose("/superset")
    def get_column_values(self) -> FlaskResponse:
        return self.response(200, result="Hello from Superset")
    # @protect()
    # @safe
    # @statsd_metrics
