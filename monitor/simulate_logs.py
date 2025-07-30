import time
import random
import json
import requests
from datetime import datetime

ELASTICSEARCH_URL = "http://localhost:9200/codepulse-logs/_doc"

def generate_log():
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "developer_id": random.choice(["dev001", "dev002", "dev003"]),
        "cpu_usage": random.uniform(10, 100),
        "memory_usage": random.uniform(1000, 16000),
        "keystrokes": random.randint(50, 500),
        "mouse_clicks": random.randint(20, 200),
        "emotion": random.choice(["neutral", "stressed", "burnout", "happy"])
    }
    return log

def send_log_to_elasticsearch(log):
    headers = {"Content-Type": "application/json"}
    response = requests.post(ELASTICSEARCH_URL, headers=headers, data=json.dumps(log))
    print(f"Sent log: {log} | Response status: {response.status_code}")

if __name__ == "__main__":
    while True:
        log = generate_log()
        send_log_to_elasticsearch(log)
        time.sleep(5)
