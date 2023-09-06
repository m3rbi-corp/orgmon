from event.team_event import TeamEvent, TeamEventAction
from threat.threat_qualifier import ThreatQualifier
from threat.threat import ThreatType

class SuspiciousTeamNamePrefixQualifier(ThreatQualifier):
    def __init__(self, prefix: str) -> None:
        self._prefix = prefix

    @classmethod
    def threat_type(cls) -> ThreatType:
        return ThreatType.SuspiciousTeamNamePrefix

    def is_threat(self, event: TeamEvent) -> bool:
        if event.action != TeamEventAction.Creation:
            return False

        return event.team.name.startswith(self._prefix)
