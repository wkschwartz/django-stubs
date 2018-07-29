from datetime import (
    date,
    datetime,
    time,
    timedelta,
)
from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.fields.files import FieldFile
from django.forms.boundfield import BoundField
from django.forms.forms import BaseForm
from django.forms.widgets import (
    ClearableFileInput,
    Input,
    Widget,
)
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)


class BaseTemporalField:
    def __init__(self, *, input_formats = ..., **kwargs) -> None: ...
    def to_python(self, value: str) -> Union[date, time]: ...


class BooleanField:
    def has_changed(self, initial: Optional[bool], data: Optional[Union[bool, str]]) -> bool: ...
    def to_python(self, value: Optional[Union[str, int]]) -> bool: ...
    def validate(self, value: bool) -> None: ...


class CallableChoiceIterator:
    def __init__(self, choices_func: Callable) -> None: ...
    def __iter__(self) -> None: ...


class CharField:
    def __init__(
        self,
        *,
        max_length = ...,
        min_length = ...,
        strip = ...,
        empty_value = ...,
        **kwargs
    ) -> None: ...
    def to_python(self, value: Optional[Union[int, Tuple, str]]) -> Optional[str]: ...
    def widget_attrs(self, widget: Widget) -> Dict[str, str]: ...


class ChoiceField:
    def __deepcopy__(self, memo: Dict[int, Any]) -> ChoiceField: ...
    def __init__(self, *, choices = ..., **kwargs) -> None: ...
    def _get_choices(self) -> Any: ...
    def _set_choices(self, value: Any) -> None: ...
    def to_python(self, value: Optional[str]) -> str: ...
    def valid_value(self, value: str) -> bool: ...
    def validate(self, value: str) -> None: ...


class ComboField:
    def __init__(self, fields: List[CharField], **kwargs) -> None: ...
    def clean(self, value: Optional[str]) -> str: ...


class DateField:
    def strptime(self, value: str, format: str) -> date: ...
    def to_python(self, value: Optional[Union[date, str]]) -> Optional[date]: ...


class DateTimeField:
    def prepare_value(self, value: Optional[datetime]) -> Optional[datetime]: ...
    def strptime(self, value: str, format: str) -> datetime: ...
    def to_python(self, value: Optional[Union[str, date]]) -> Optional[datetime]: ...


class DecimalField:
    def __init__(
        self,
        *,
        max_value = ...,
        min_value = ...,
        max_digits = ...,
        decimal_places = ...,
        **kwargs
    ) -> None: ...
    def to_python(self, value: Optional[Union[str, float]]) -> Optional[Decimal]: ...
    def validate(self, value: Decimal) -> None: ...
    def widget_attrs(self, widget: Widget) -> Dict[str, str]: ...


class DurationField:
    def prepare_value(self, value: Optional[timedelta]) -> Optional[str]: ...
    def to_python(self, value: Union[str, int]) -> timedelta: ...


class EmailField:
    def __init__(self, **kwargs) -> None: ...


class Field:
    def __deepcopy__(self, memo: Dict[int, Any]) -> Field: ...
    def __init__(
        self,
        *,
        required = ...,
        widget = ...,
        label = ...,
        initial = ...,
        help_text = ...,
        error_messages = ...,
        show_hidden_initial = ...,
        validators = ...,
        localize = ...,
        disabled = ...,
        label_suffix = ...
    ) -> None: ...
    def bound_data(self, data: Any, initial: Any) -> Any: ...
    def clean(self, value: Any) -> Any: ...
    def get_bound_field(self, form: BaseForm, field_name: str) -> BoundField: ...
    def has_changed(self, initial: Any, data: Optional[str]) -> bool: ...
    def prepare_value(self, value: Any) -> Any: ...
    def run_validators(self, value: Any) -> None: ...
    def to_python(self, value: Any) -> Any: ...
    def validate(self, value: Any) -> None: ...
    def widget_attrs(self, widget: Widget) -> Dict[Any, Any]: ...


class FileField:
    def __init__(self, *, max_length = ..., allow_empty_file = ..., **kwargs) -> None: ...
    def bound_data(
        self,
        data: Union[str, SimpleUploadedFile],
        initial: None
    ) -> Union[str, SimpleUploadedFile]: ...
    def clean(
        self,
        data: Optional[Union[str, bool, SimpleUploadedFile]],
        initial: Optional[Union[str, FieldFile]] = ...
    ) -> Any: ...
    def has_changed(self, initial: Union[str, FieldFile], data: Optional[str]) -> bool: ...
    def to_python(
        self,
        data: Optional[Union[str, SimpleUploadedFile]]
    ) -> Optional[SimpleUploadedFile]: ...


class FilePathField:
    def __init__(
        self,
        path: str,
        *,
        match = ...,
        recursive = ...,
        allow_files = ...,
        allow_folders = ...,
        **kwargs
    ) -> None: ...


class FloatField:
    def to_python(self, value: str) -> Optional[float]: ...
    def validate(self, value: Optional[float]) -> None: ...
    def widget_attrs(self, widget: Input) -> Dict[str, Union[int, str]]: ...


class GenericIPAddressField:
    def __init__(self, *, protocol = ..., unpack_ipv4 = ..., **kwargs) -> None: ...
    def to_python(self, value: str) -> str: ...


class ImageField:
    def widget_attrs(self, widget: ClearableFileInput) -> Dict[str, str]: ...


class IntegerField:
    def __init__(self, *, max_value = ..., min_value = ..., **kwargs) -> None: ...
    def to_python(self, value: Optional[Union[float, int, str]]) -> Optional[int]: ...
    def widget_attrs(self, widget: Input) -> Dict[str, Union[Decimal, int]]: ...


class MultiValueField:
    def __deepcopy__(self, memo: Dict[int, Any]) -> MultiValueField: ...
    def __init__(
        self,
        fields: Union[Tuple[DateField, TimeField], Tuple[CharField, MultipleChoiceField, SplitDateTimeField], Tuple[CharField, CharField]],
        *,
        require_all_fields = ...,
        **kwargs
    ) -> None: ...
    def clean(
        self,
        value: Union[str, List[Union[str, List[str]]], List[str]]
    ) -> Optional[Union[str, datetime]]: ...
    def has_changed(
        self,
        initial: Optional[Union[datetime, List[None], List[str]]],
        data: Union[List[None], List[str]]
    ) -> bool: ...
    def validate(self, value: Union[str, datetime]) -> None: ...


class MultipleChoiceField:
    def has_changed(self, initial: Optional[Union[str, List[int]]], data: Union[str, List[str]]) -> bool: ...
    def to_python(self, value: Optional[Union[Tuple, str, List[str]]]) -> List[str]: ...
    def validate(self, value: List[str]) -> None: ...


class NullBooleanField:
    def to_python(self, value: Optional[Union[str, bool]]) -> Optional[bool]: ...
    def validate(self, value: Optional[bool]) -> None: ...


class RegexField:
    def __init__(self, regex: str, **kwargs) -> None: ...
    def _set_regex(self, regex: str) -> None: ...


class SlugField:
    def __init__(self, *, allow_unicode = ..., **kwargs) -> None: ...


class SplitDateTimeField:
    def __init__(self, *, input_date_formats = ..., input_time_formats = ..., **kwargs) -> None: ...
    def compress(self, data_list: List[Union[date, time]]) -> Optional[datetime]: ...


class TimeField:
    def strptime(self, value: str, format: str) -> time: ...
    def to_python(self, value: Optional[Union[str, time]]) -> Optional[time]: ...


class TypedChoiceField:
    def __init__(self, *, coerce = ..., empty_value = ..., **kwargs) -> None: ...
    def _coerce(self, value: Optional[Union[str, int]]) -> Optional[Union[int, str]]: ...
    def clean(self, value: Optional[str]) -> Optional[Union[str, int]]: ...


class TypedMultipleChoiceField:
    def __init__(self, *, coerce = ..., **kwargs) -> None: ...
    def _coerce(self, value: List[str]) -> Optional[Union[List[Decimal], List[int]]]: ...
    def clean(self, value: List[str]) -> Optional[Union[List[bool], List[int]]]: ...
    def validate(self, value: List[str]) -> None: ...


class URLField:
    def __init__(self, **kwargs) -> None: ...
    def to_python(self, value: Optional[Union[str, int]]) -> Optional[str]: ...