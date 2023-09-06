import dataclasses
import enum

from .event import OrganizationEvent
from .event_type import EventType


class TeamEventAction(enum.Enum):
    Delete = 'deleted'
    Creation = 'created'


@dataclasses.dataclass
class TeamRecord:
    name: str


@dataclasses.dataclass
class TeamEvent(OrganizationEvent):
    action: TeamEventAction
    team: TeamRecord
    
    @classmethod
    def event_type(cls) -> EventType:
        return EventType.TeamEvent
