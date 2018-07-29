from datetime import date
from django.core.checks.messages import (
    Error,
    Warning,
)
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model
from django.db.models.expressions import OuterRef
from django.db.models.sql.compiler import SQLCompiler
from django.forms.fields import (
    BaseTemporalField,
    BooleanField,
    CharField,
    IntegerField,
    SplitDateTimeField,
    TypedChoiceField,
)
from typing import (
    Any,
    List,
    Optional,
    Union,
)


class AutoField:
    def __init__(self, *args, **kwargs) -> None: ...
    def _check_primary_key(self) -> List[Any]: ...
    def check(self, **kwargs) -> List[Any]: ...
    def contribute_to_class(self, cls: Any, name: str, **kwargs) -> None: ...
    def deconstruct(self) -> Any: ...
    def formfield(self, **kwargs) -> None: ...
    def get_db_prep_value(
        self,
        value: Union[str, int],
        connection: DatabaseWrapper,
        prepared: bool = ...
    ) -> Union[str, int]: ...
    def get_internal_type(self) -> str: ...
    def get_prep_value(self, value: Any) -> Optional[Union[int, OuterRef]]: ...
    def rel_db_type(self, connection: DatabaseWrapper) -> str: ...
    def to_python(self, value: Optional[Union[str, int]]) -> Optional[int]: ...
    def validate(self, value: int, model_instance: Model) -> None: ...


class BigAutoField:
    def get_internal_type(self) -> str: ...
    def rel_db_type(self, connection: DatabaseWrapper) -> str: ...


class BigIntegerField:
    def formfield(self, **kwargs) -> IntegerField: ...
    def get_internal_type(self) -> str: ...


class BinaryField:
    def __init__(self, *args, **kwargs) -> None: ...
    def deconstruct(self) -> Any: ...
    def get_db_prep_value(
        self,
        value: Optional[Union[bytes, memoryview]],
        connection: DatabaseWrapper,
        prepared: bool = ...
    ) -> Optional[memoryview]: ...
    def get_default(self) -> Optional[bytes]: ...
    def get_internal_type(self) -> str: ...
    def get_placeholder(
        self,
        value: Optional[memoryview],
        compiler: SQLCompiler,
        connection: DatabaseWrapper
    ) -> str: ...
    def to_python(self, value: Optional[Union[str, bytes]]) -> Optional[Union[bytes, memoryview]]: ...


class BooleanField:
    def formfield(self, **kwargs) -> BooleanField: ...
    def get_internal_type(self) -> str: ...
    def get_prep_value(self, value: Optional[Union[str, int]]) -> Optional[bool]: ...
    def to_python(self, value: Optional[Union[str, int]]) -> bool: ...


class CharField:
    def __init__(self, *args, **kwargs) -> None: ...
    def _check_max_length_attribute(self, **kwargs) -> List[Error]: ...
    def check(self, **kwargs) -> List[Error]: ...
    def formfield(self, **kwargs) -> Union[CharField, TypedChoiceField]: ...
    def get_internal_type(self) -> str: ...
    def get_prep_value(self, value: Any) -> object: ...
    def to_python(self, value: Optional[Union[int, str, Model]]) -> Optional[str]: ...


class DateField:
    def __init__(
        self,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        auto_now: bool = ...,
        auto_now_add: bool = ...,
        **kwargs
    ) -> None: ...
    def _check_fix_default_value(self) -> List[Warning]: ...
    def contribute_to_class(self, cls: Any, name: str, **kwargs) -> None: ...
    def deconstruct(self) -> Any: ...
    def formfield(
        self,
        **kwargs
    ) -> Union[SplitDateTimeField, BaseTemporalField]: ...
    def get_db_prep_value(
        self,
        value: Optional[Union[date, str]],
        connection: DatabaseWrapper,
        prepared: bool = ...
    ) -> Optional[str]: ...
    def get_internal_type(self) -> str: ...
    def get_prep_value(self, value: Optional[Union[str, date]]) -> Optional[date]: ...
    def pre_save(self, model_instance: Model, add: bool) -> Optional[date]: ...