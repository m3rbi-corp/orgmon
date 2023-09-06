import enum


class EventType(enum.Enum):
    InvalidEvent = 0
    PushEvent = 1
    TeamEvent = 2
    RepoEvent = 3
