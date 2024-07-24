import logging
from flask_appbuilder.api import expose, protect, safe
from views.base_api import BaseSupersetApi, statsd_metrics
from superset_typing import FlaskResponse

logger = logging.getLogger(__name__)


class DatasourceRestApi(BaseSupersetApi):
    allow_browser_login = True
    class_permission_name = "Datasource"
    resource_name = "datasource"
    openapi_spec_tag = "Datasources"

    @expose(
            "/<datasource_type>/<int:datasource_id>/column/<column_name>/values/",
            methods=("GET",),
        )
    @protect()
    @safe
    @statsd_metrics
    def get_column_values(
        self, datasource_type: str, datasource_id: int, column_name: str
    ) -> FlaskResponse:
        return self.response(200, result="Hello world")