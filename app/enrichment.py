from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any


class LogEntry(BaseModel):
    timestamp: datetime
    level: str = Field(..., regex="^(INFO|WARNING|ERROR|DEBUG)$")
    message: str
    service_name: str
    properties: Optional[Dict[str, Any]] = {}


class EnrichedLogEntry(LogEntry):
    ingestion_time: datetime
    environment: str
    instance_id: str