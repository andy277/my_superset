import os
from typing import Any
from werkzeug.local import LocalProxy


from flask_appbuilder import AppBuilder

APP_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
appbuilder = AppBuilder()
_event_logger: dict[str, Any] = {}
event_logger = LocalProxy(lambda: _event_logger.get("event_logger"))

