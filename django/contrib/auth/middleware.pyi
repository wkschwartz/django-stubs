from django.contrib.auth.models import (
    AnonymousUser,
    User,
)
from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from typing import Union


def get_user(
    request: HttpRequest
) -> Union[AnonymousUser, User]: ...


class AuthenticationMiddleware:
    def process_request(self, request: HttpRequest) -> None: ...


class RemoteUserMiddleware:
    def _remove_invalid_user(self, request: WSGIRequest) -> None: ...
    def clean_username(self, username: str, request: WSGIRequest) -> str: ...
    def process_request(self, request: WSGIRequest) -> None: ...