from typing import (
    Any,
    Dict,
)


def check_password(environ: Dict[Any, Any], username: str, password: str): ...


def groups_for_user(environ: Dict[Any, Any], username: str): ...