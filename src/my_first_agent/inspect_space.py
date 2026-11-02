import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
SPACE_ID = os.getenv("HF_SPACE_ID")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found in .env")

if not SPACE_ID:
    raise ValueError("HF_SPACE_ID is missing")

BASE_URL = f"https://{SPACE_ID.replace('/', '-')}.hf.space"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def get_json(endpoint: str) -> dict:
    url = f"{BASE_URL}{endpoint}"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30,
    )

    print(f"{endpoint}: HTTP {response.status_code}")

    response.raise_for_status()

    return response.json()


# Discover API schema
api_info = get_json("/gradio_api/info")

print("\n===== API SCHEMA =====")
print(json.dumps(api_info, indent=2))


# Discover Gradio dependency IDs
config = get_json("/config")

print("\n===== AVAILABLE API ENDPOINTS =====")

for dependency in config.get("dependencies", []):
    api_name = dependency.get("api_name")

    if api_name:
        print(
            f"API name: {api_name}"
            f" | Dependency ID: {dependency.get('id')}"
        )