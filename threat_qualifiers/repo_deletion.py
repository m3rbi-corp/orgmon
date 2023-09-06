import datetime

from event.repo_event import RepoEvent, RepoEventAction
from threat.threat_qualifier import ThreatQualifier
from threat.threat import ThreatType


class RepoDeletionQualifier(ThreatQualifier):
    def __init__(self, delta: datetime.timedelta) -> None:
        self._delta = delta

    @classmethod
    def threat_type(cls) -> ThreatType:
        return ThreatType.RepoDeletion

    def is_threat(self, event: RepoEvent) -> bool:
        if event.action != RepoEventAction.Delete:
            return False
        
        return (event.repository.updated_at - event.repository.created_at) <= self._delta
