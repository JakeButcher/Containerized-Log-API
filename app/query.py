import json
from collections import Counter
from .storage import container_client


async def get_logs(limit: int = 100):
    logs = []
    blobs = container_client.list_blobs()

    for i, blob in enumerate(blobs):
        if i >= limit:
            break

        blob_client = container_client.get_blob_client(blob.name)
        data = blob_client.download_blob().readall()
        logs.append(json.loads(data))

    return logs


async def aggregate_by_level():
    blobs = container_client.list_blobs()
    counter = Counter()

    for blob in blobs:
        blob_client = container_client.get_blob_client(blob.name)
        data = blob_client.download_blob().readall()
        log = json.loads(data)
        counter[log["level"]] += 1

    return dict(counter)