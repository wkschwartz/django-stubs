from typing import (
    Any,
    List,
)


class LazySettings:
    def __delattr__(self, name: str) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: object) -> None: ...
    def _setup(self, name: None = ...): ...
    def configure(self, default_settings: Any = ..., **options): ...
    @property
    def configured(self) -> bool: ...


class Settings:
    def __init__(self, settings_module: str): ...
    def is_overridden(self, setting: str) -> bool: ...


class UserSettingsHolder:
    def __delattr__(self, name: str) -> None: ...
    def __dir__(self) -> List[str]: ...
    def __getattr__(self, name: str) -> Any: ...
    def __init__(self, default_settings: Any) -> None: ...
    def __setattr__(self, name: str, value: Any) -> None: ...