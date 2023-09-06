from typing import Dict, List
from threat.threat_detector import ThreatDetector
from event.event import OrganizationEvent
from event.event_type import EventType
from threat.threat import Threat


class EventProcessor:
    def __init__(self, threat_detecors: Dict[EventType, List[ThreatDetector]]) -> None:
        self._detectors = threat_detecors
    
    def process(self, event: OrganizationEvent) -> None:
        relevant_detectors = self._detectors.get(event.event_type())
        if not relevant_detectors:
            return
        
        for detector in relevant_detectors:
            if detector.qualifier.is_threat(event):
                detector.handler.handle_threat(Threat(detector.qualifier.threat_type(), event))
