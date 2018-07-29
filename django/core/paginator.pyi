from django.db.models.base import Model
from django.db.models.query import QuerySet
from typing import (
    List,
    Optional,
    Union,
)


class Page:
    def __getitem__(self, index: Union[slice, int]) -> Union[str, List[Model]]: ...
    def __init__(
        self,
        object_list: Union[QuerySet, str, List[object], List[int]],
        number: int,
        paginator: Paginator
    ) -> None: ...
    def __repr__(self) -> str: ...
    def end_index(self) -> int: ...
    def has_next(self) -> bool: ...
    def has_other_pages(self) -> bool: ...
    def has_previous(self) -> bool: ...
    def next_page_number(self) -> int: ...
    def previous_page_number(self) -> int: ...
    def start_index(self) -> int: ...


class Paginator:
    def __init__(
        self,
        object_list: Union[List[object], QuerySet, List[int]],
        per_page: Union[str, int],
        orphans: Union[str, int] = ...,
        allow_empty_first_page: bool = ...
    ) -> None: ...
    def _check_object_list_is_ordered(self) -> None: ...
    def _get_page(self, *args, **kwargs) -> Page: ...
    @cached_property
    def count(self) -> int: ...
    def get_page(self, number: Optional[int]) -> Page: ...
    @cached_property
    def num_pages(self) -> int: ...
    def page(self, number: Union[str, int]) -> Page: ...
    @property
    def page_range(self) -> range: ...
    def validate_number(self, number: Optional[Union[str, float, int]]) -> int: ...