import dataclasses
from typing import List
import datetime

from .event import OrganizationEvent
from .event_type import EventType

@dataclasses.dataclass
class CommitRecord:
    timestamp: datetime.datetime

@dataclasses.dataclass
class PushEvent(OrganizationEvent):
    commits: List[CommitRecord]

    @classmethod
    def event_type(cls) -> EventType:
        return EventType.PushEvent
