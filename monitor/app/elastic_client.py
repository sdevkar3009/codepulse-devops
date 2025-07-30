import httpx
import datetime

ELASTIC_URL = "http://localhost:9200/github-events/_doc"

async def send_to_elasticsearch(data):
    data["@timestamp"] = datetime.datetime.utcnow().isoformat()
    async with httpx.AsyncClient() as client:
        response = await client.post(ELASTIC_URL, json=data)
        if response.status_code not in [200, 201]:
            print("Failed to send data to Elasticsearch:", response.text)
