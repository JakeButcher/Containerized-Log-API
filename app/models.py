from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, Dict, Any


class LogEntry(BaseModel):
    timestamp: datetime
    level: str
    message: str
    service_name: str
    properties: Optional[Dict[str, Any]] = {}

    @validator("level")
    def normalize_level(cls, v):
        allowed = {"INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"}
        v = v.upper()
        if v not in allowed:
            raise ValueError(f"level must be one of {allowed}")
        return v


class EnrichedLogEntry(LogEntry):
    ingestion_time: datetime
    environment: str
    instance_id: str
    log_type: str
    severity_score: int