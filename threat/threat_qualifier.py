import abc
from event.event import OrganizationEvent
from .threat import ThreatType


class ThreatQualifier(abc.ABC):
    @abc.abstractclassmethod
    def threat_type(cls) -> ThreatType:
        raise NotImplementedError()
        
    @abc.abstractmethod
    def is_threat(self, event: OrganizationEvent) -> bool:
        raise NotImplementedError
