

import os

from dotenv import load_dotenv
from gradio_client import Client

# Load environment variables
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
SPACE_ID = os.getenv("HF_SPACE_ID")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is missing")

if not SPACE_ID:
    raise ValueError("HF_SPACE_ID is missing")

# Connect to the configured Hugging Face Space
client = Client(
    SPACE_ID,
    token=HF_TOKEN,
)

# Send a request to Qwen
response = client.predict(
    "What is an AI Agent? Explain in simple English.",
    "You are a helpful AI assistant. Give clear and concise answers.",
    128,
    0.7,
    0.95,
    api_name="/respond",
)

print("\n===== QWEN RESPONSE =====")
print(response)
