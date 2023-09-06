import dataclasses
from .threat_qualifier import ThreatQualifier
from .threat_handler import ThreatHandler


@dataclasses.dataclass
class ThreatDetector:
    qualifier: ThreatQualifier
    handler: ThreatHandler
