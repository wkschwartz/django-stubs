from collections import OrderedDict
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.expressions import Col
from django.db.models.fields import (
    AutoField,
    IntegerField,
)
from django.db.models.fields.related import (
    ForeignKey,
    ForeignObject,
)
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.query import Query
from typing import (
    Any,
    List,
    Tuple,
    Type,
    Union,
)
from uuid import UUID


def get_normalized_value(
    value: Any,
    lhs: Union[MultiColSource, Col]
) -> Any: ...


class MultiColSource:
    def __init__(
        self,
        alias: str,
        targets: Union[Tuple[IntegerField, related.ForeignKey], Tuple[IntegerField, IntegerField]],
        sources: Union[Tuple[AutoField, IntegerField], Tuple[IntegerField, AutoField]],
        field: related.ForeignObject
    ) -> None: ...
    def get_lookup(
        self,
        lookup: str
    ) -> Type[Union[RelatedIn, RelatedExact]]: ...
    def relabeled_clone(
        self,
        relabels: OrderedDict
    ) -> MultiColSource: ...


class RelatedIn:
    def as_sql(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper
    ) -> Union[Tuple[str, List[int]], Tuple[str, List[Any]], Tuple[str, List[str]]]: ...
    def get_prep_lookup(self) -> Union[List[UUID], Query, List[int], List[str]]: ...


class RelatedLookupMixin:
    def as_sql(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper
    ) -> Union[Tuple[str, List[int]], Tuple[str, List[Any]], Tuple[str, List[str]]]: ...
    def get_prep_lookup(self) -> Any: ...