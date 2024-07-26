import logging
from flask_appbuilder.api import expose, protect, safe, BaseApi
from superset.views.base_api import BaseSupersetApi, statsd_metrics
from superset.superset_typing import FlaskResponse
from typing import Dict

logger = logging.getLogger(__name__)


class DatasourceRestApi(BaseApi):
    # route_base = "/api"
    # allow_browser_login = True
    # class_permission_name = "Datasource"
    resource_name = "datasource"
    # openapi_spec_tag = "Datasources"

    @expose("/superset", methods=['GET'])
    def get_column_values(self) -> Dict:
        message = {"message": "Hello world"}
        return message
    # @protect()
    # @safe
    # @statsd_metrics
