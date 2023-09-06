import dataclasses
import enum
import datetime

from .event import OrganizationEvent
from .event_type import EventType


class RepoEventAction(enum.Enum):
    Delete = 'deleted'
    Creation = 'created'


@dataclasses.dataclass
class RepositoryRecord:
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclasses.dataclass
class RepoEvent(OrganizationEvent):
    action: RepoEventAction
    repository: RepositoryRecord

    @classmethod
    def event_type(cls) -> EventType:
        return EventType.RepoEvent
