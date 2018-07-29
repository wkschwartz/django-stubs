from django.template.base import (
    Parser,
    Token,
)
from django.template.context import Context


def get_admin_log(
    parser: Parser,
    token: Token
) -> AdminLogNode: ...


class AdminLogNode:
    def __init__(self, limit: str, varname: str, user: str) -> None: ...
    def render(self, context: Context) -> str: ...