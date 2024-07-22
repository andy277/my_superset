from typing import Optional
from flask import Flask


def create_app(superset_config_module: Optional[str] = None) -> Flask:
    app = SupersetApp(__name__)


class SupersetApp(Flask):
    pass
