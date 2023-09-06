import abc
from threat.threat import Threat


class ThreatHandler(abc.ABC):
    @abc.abstractmethod
    def handle_threat(cls, threat: Threat) -> None:
        raise NotImplementedError
