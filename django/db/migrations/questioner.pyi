from django.db.migrations.state import ModelState
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from typing import (
    Dict,
    Optional,
    Set,
    Union,
)


class InteractiveMigrationQuestioner:
    def _ask_default(self, default: str = ...) -> int: ...
    def _boolean_input(self, question: str, default: bool = ...) -> bool: ...
    def ask_auto_now_add_addition(self, field_name: str, model_name: str) -> int: ...
    def ask_not_null_addition(self, field_name: str, model_name: str) -> None: ...


class MigrationQuestioner:
    def __init__(
        self,
        defaults: Optional[Dict[str, bool]] = ...,
        specified_apps: Optional[Set[str]] = ...,
        dry_run: Optional[bool] = ...
    ) -> None: ...
    def ask_auto_now_add_addition(self, field_name: str, model_name: str) -> None: ...
    def ask_initial(self, app_label: str) -> bool: ...
    def ask_not_null_addition(self, field_name: str, model_name: str) -> None: ...
    def ask_rename(
        self,
        model_name: str,
        old_name: str,
        new_name: str,
        field_instance: Union[IntegerField, related.ForeignKey]
    ) -> bool: ...
    def ask_rename_model(
        self,
        old_model_state: ModelState,
        new_model_state: ModelState
    ) -> bool: ...