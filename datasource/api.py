import logging
from flask_appbuilder.api import expose, protect, safe
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
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}"
                                             f".get_column_values",
        log_to_statsd=False,
    )
    def get_column_values(
        self, datasource_type: str, datasource_id: int, column_name: str
    ) -> FlaskResponse:
        return self.response(200, result="Hello world")