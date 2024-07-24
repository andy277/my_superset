from flask import current_app, Flask
from werkzeug.local import LocalProxy

from app import create_app
from extensions import (
    appbuilder,
    event_logger
)

app: Flask = current_app