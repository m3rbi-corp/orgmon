import uvicorn
from fastapi import FastAPI, Request
from datetime import time, timedelta
from pydantic_core._pydantic_core import TzInfo

from event.event_type import EventType
from event.push_event import PushEvent
from event.team_event import TeamEvent
from event.repo_event import RepoEvent


from threat.threat_detector import ThreatDetector
from event_processor.event_processor import EventProcessor

from threat_qualifiers.repo_deletion import RepoDeletionQualifier
from threat_qualifiers.suspicious_team_name import SuspiciousTeamNamePrefixQualifier
from threat_qualifiers.suspicious_time_push import SuspiciousTimePushQualifier

from threat_handlers.console_handler import ConsoleThreatHandler


app = FastAPI()
import json


DETECTORS = {
    EventType.PushEvent: [ThreatDetector(SuspiciousTimePushQualifier(time(19), time(20), TzInfo(3*60*60)), ConsoleThreatHandler())],
    EventType.RepoEvent: [ThreatDetector(RepoDeletionQualifier(delta=timedelta(seconds=200)), ConsoleThreatHandler())],
    EventType.TeamEvent: [ThreatDetector(SuspiciousTeamNamePrefixQualifier("hacker"), ConsoleThreatHandler())]
}

EVENT_PROCESSOR = EventProcessor(DETECTORS)


@app.post("/push_event")
def handle_push(push_event: PushEvent):
    EVENT_PROCESSOR.process(push_event)

@app.post("/repo_event")
def handle_repo(repo_event: RepoEvent):
    EVENT_PROCESSOR.process(repo_event)

@app.post("/team_event")
def handle_team(team_event: TeamEvent):
    EVENT_PROCESSOR.process(team_event)

def main():
    uvicorn.run(app, host="0.0.0.0", port=1337)


if __name__ == '__main__':
    main()
