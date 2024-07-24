import logging
from typing import Optional
from flask import Flask
import os

from initialization import SupersetAppInitializer


logger = logging.getLogger(__name__)


def create_app(superset_config_module: Optional[str] = None) -> Flask:
    app = SupersetApp(__name__)

    try:
        config_module = superset_config_module or os.environ.get("SUPERSET_CONFIG_MODULE", "superset.config")
        app.config.from_object(config_module)

        app_initializer = app.config.get("APP_INITIALIZER", SupersetAppInitializer)(app)
        app_initializer.init_app()

        return app

    except Exception as ex:
        logger.exception("Fail to create app")
        raise ex


class SupersetApp(Flask):
    pass
