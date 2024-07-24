from typing import Any, TYPE_CHECKING

from deprecation import deprecated
from extensions import appbuilder


if TYPE_CHECKING:
    from app import SupersetApp

class SupersetAppInitializer:
    def __init__(self, app: SupersetApp) -> None:
        super().__init__()

        self.superset_app = app
        self.config = app.config

        self.manifest: dict[Any, Any] = {}

    @deprecated(details="use self.superset_app instead of self.flask_app")  # type: ignore
    @property
    def flask_app(self) -> SupersetApp:
        return self.superset_app

    def init_views(self) -> None:
        from datasource.api import DatasourceRestApi

        #
        # Setup API views
        #
        appbuilder.add_api(DatasourceRestApi)

