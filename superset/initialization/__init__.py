from typing import Any
from flask import Flask
import logging
from deprecation import deprecated
from superset.extensions import appbuilder

#if TYPE_CHECKING:
# from superset.app import SupersetApp

logger = logging.getLogger(__name__)


class SupersetAppInitializer:
    def __init__(self, app: Flask) -> None:  # pylint: disable=too-many-public-methods
        super().__init__()

        self.superset_app = app
        self.config = app.config
        self.manifest: dict[Any, Any] = {}

    @deprecated(details="use self.superset_app instead of self.flask_app")  # type: ignore
    @property
    def flask_app(self) -> Flask:
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
        self.register_blueprints()

    def register_blueprints(self) -> None:
        for bp in self.config["BLUEPRINTS"]:
            try:
                logger.info("Registering blueprint: %s", bp.name)
                self.superset_app.register_blueprint(bp)
            except Exception:  # pylint: disable=broad-except
                logger.exception("blueprint registration failed")
