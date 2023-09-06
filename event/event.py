import dataclasses
from typing import Dict
import abc

from .event_type import EventType


@dataclasses.dataclass
class OrganizationEvent(abc.ABC):
    @abc.abstractclassmethod
    def event_type(cls) -> EventType:
        raise NotImplementedError()
