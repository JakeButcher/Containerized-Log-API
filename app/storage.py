import json
from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
from datetime import datetime
from .config import AZURE_STORAGE_ACCOUNT_URL, AZURE_STORAGE_CONTAINER

credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(
    account_url=AZURE_STORAGE_ACCOUNT_URL,
    credential=credential,
)

container_client = blob_service_client.get_container_client(
    AZURE_STORAGE_CONTAINER
)


async def store_log(log_data: dict):
    blob_name = f"{datetime.utcnow().isoformat()}-{log_data['service_name']}.json"
    blob_client = container_client.get_blob_client(blob_name)

    blob_client.upload_blob(
        json.dumps(log_data),
        overwrite=True,
    )