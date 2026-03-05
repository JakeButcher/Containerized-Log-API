# Containerized-Log-API

Containerized Python FastAPI service that receives log data (JSON) from Azure, enriches it with metadata, stores it in Blob Storage, and exposes endpoints to query aggregated results.  The API deploys to Azure Container Apps, scales automatically, and is fully observable with Azure Monitor + Application Insights.

```
Using Azure Container Apps



Applications send JSON logs
        ↓
Pydantic Validation
        ↓
Metadata Enrichment
        ↓
Azure Blob Storage
        ↓
Query + Aggregation Endpoints

```
