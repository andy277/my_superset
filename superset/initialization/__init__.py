from typing import Any
from flask import Flask
from deprecation import deprecated
from superset.extensions import appbuilder

#if TYPE_CHECKING:
# from superset.app import SupersetApp


class SupersetAppInitializer:
    def __init__(self, app: Flask) -> None:  # pylint: disable=too-many-public-methods
        super().__init__()

        self.superset_app = app
        self.config = app.config
        self.manifest: dict[Any, Any] = {}

    @deprecated(details="use self.superset_app instead of self.flask_app")  # type: ignore
    @property
    def flask_app(self) ->  Flask:
        return self.superset_app

    def init_views(self) -> None:
        from superset.datasource.api import DatasourceRestApi

        #
        # Setup API views
        #
        appbuilder.add_api(DatasourceRestApi)

    def init_app(self) -> None:
        """
              Main entry point which will delegate to other methods in
              order to fully init the app
        """
        self.init_views()
        # for rule in self.superset_app.url_map.iter_rules():
        #     print(rule)

