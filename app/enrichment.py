from datetime import datetime
import os
import socket
from .models import LogEntry, EnrichedLogEntry


def enrich_log(log: LogEntry) -> EnrichedLogEntry:
    return EnrichedLogEntry(
        **log.dict(),
        ingestion_time=datetime.utcnow(),
        environment=os.getenv("ENVIRONMENT", "production"),
        instance_id=socket.gethostname(),
    )