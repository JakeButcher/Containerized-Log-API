from fastapi import FastAPI, HTTPException
from typing import List
from .models import LogEntry
from .enrichment import enrich_log
from .storage import store_log
from .query import get_logs, aggregate_by_level
from .config import APPLICATIONINSIGHTS_CONNECTION_STRING

from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

app = FastAPI(title="Azure Log Processing Service")


# Application Insights logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if APPLICATIONINSIGHTS_CONNECTION_STRING:
    logger.addHandler(
        AzureLogHandler(
            connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING
        )
    )


@app.post("/logs")
async def ingest_log(log: LogEntry):
    try:
        enriched = enrich_log(log)
        await store_log(enriched.dict())

        logger.info("Log ingested", extra=enriched.dict())
        return {"status": "success"}

    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Log ingestion failed")


@app.get("/logs")
async def read_logs(limit: int = 100):
    return await get_logs(limit)


@app.get("/logs/aggregate")
async def aggregate_logs():
    return await aggregate_by_level()


@app.get("/health")
async def health_check():
    return {"status": "healthy"}