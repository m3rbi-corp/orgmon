from datetime import time
from pydantic_core._pydantic_core import TzInfo

from threat.threat_qualifier import ThreatQualifier
from threat.threat import ThreatType

from event.push_event import PushEvent


class SuspiciousTimePushQualifier(ThreatQualifier):
    """
    Note! when initializing this object, we need to have a consecutive time window during the day.
    For example, if we'd like to notice events occuring between 22:00 and 1:00 the day after 
    we'll need to use 2 instances, one for 22:00-00:00 and one for 1:00.
    """
    def __init__(self, start_time: time, end_time: time, timezone: TzInfo) -> None:
        if start_time > end_time and end_time != time(0):
            raise ValueError("Cannot set start time to be after end time")

        self._start_time = start_time
        self._end_time = end_time
        self._tz = timezone

    @classmethod
    def threat_type(cls) -> ThreatType:
        return ThreatType.SuspiciousTimePush

    def is_threat(self, event: PushEvent) -> bool:
        all_times = [commit.timestamp.astimezone(self._tz).time() for commit in event.commits]
        for t in all_times:
            if t >= self._start_time and (self._end_time == time(0) or t <= self._end_time):
                    return True

        return False

