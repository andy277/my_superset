from typing import Any, Literal, Optional, TYPE_CHECKING, TypedDict, Union
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