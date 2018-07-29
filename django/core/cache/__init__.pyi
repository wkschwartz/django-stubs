from collections import OrderedDict
from django.core.cache.backends.base import BaseCache
from typing import (
    Callable,
    Dict,
    Union,
)


def _create_cache(backend: str, **kwargs) -> BaseCache: ...


def close_caches(**kwargs) -> None: ...


class CacheHandler:
    def __getitem__(self, alias: str) -> BaseCache: ...


class DefaultCacheProxy:
    def __contains__(self, key: str) -> bool: ...
    def __getattr__(self, name: str) -> Union[OrderedDict, Callable, Dict[str, float]]: ...
    def __setattr__(self, name: str, value: Callable) -> None: ...