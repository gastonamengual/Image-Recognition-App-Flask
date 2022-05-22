from dataclasses import dataclass

from abc import ABC
from typing import Generic, TypeVar

@dataclass
class AbstractModelConfig(ABC):
    ...

T = TypeVar('T', bound=AbstractModelConfig)

@dataclass
class AbstractModel(ABC, Generic[T]):

    config: T 