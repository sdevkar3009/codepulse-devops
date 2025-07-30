import json
from app.elastic_client import send_to_elasticsearch

async def handle_github_event(payload):
    event_type = payload.get("action", "unknown")
    repo = payload.get("repository", {}).get("full_name", "unknown")
    sender = payload.get("sender", {}).get("login", "unknown")

    event_data = {
        "event_type": event_type,
        "repository": repo,
        "sender": sender,
        "raw": payload,
    }

    await send_to_elasticsearch(event_data)
