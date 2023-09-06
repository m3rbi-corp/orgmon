import dataclasses
import enum
from event.event import OrganizationEvent


class ThreatType(enum.Enum):
    SuspiciousTimePush = 0
    SuspiciousTeamNamePrefix = 1
    RepoDeletion = 2


@dataclasses.dataclass
class Threat:
    threat_type: ThreatType
    event: OrganizationEvent
