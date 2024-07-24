from flask_appbuilder import AppBuilder
from typing import Any

app_builder = AppBuilder(update_perms=False)
_event_logger: dict[str, Any] = {}
