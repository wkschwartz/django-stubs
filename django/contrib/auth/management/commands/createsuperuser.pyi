from django.core.management.base import CommandParser
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from typing import (
    Optional,
    Union,
)


class Command:
    def __init__(self, *args, **kwargs) -> None: ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    def execute(self, *args, **options) -> None: ...
    def get_input_data(
        self,
        field: Union[CharField, related.ForeignKey],
        message: str,
        default: Optional[str] = ...
    ) -> Optional[str]: ...
    def handle(self, *args, **options) -> None: ...