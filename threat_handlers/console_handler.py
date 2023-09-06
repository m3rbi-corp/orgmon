from threat.threat_handler import ThreatHandler
from threat.threat import Threat


class ConsoleThreatHandler(ThreatHandler):
    def handle_threat(cls,  threat: Threat) -> None:
        print(f"Found new threat of type {threat.threat_type.name}")
