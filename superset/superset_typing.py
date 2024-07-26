from typing import Any, Union
from werkzeug.wrappers import Response


Base = Union[bytes, str]
Status = Union[int, str]
Headers = dict[str, Any]
FlaskResponse = Union[
    Response,
    Base,
    tuple[Base, Status],
    tuple[Base, Status, Headers],
    tuple[Response, Status],
]