


import os

from dotenv import load_dotenv
from gradio_client import Client

load_dotenv()

token = os.getenv("HF_TOKEN")
SPACE_ID = os.getenv("HF_SPACE_ID")

if not token:
    raise ValueError("HF_TOKEN is missing")

if not SPACE_ID:
    raise ValueError("HF_SPACE_ID is missing")

# Connect to the configured Hugging Face Space
client = Client(
    SPACE_ID,
    token=token,
)

print("\nConnected to Hugging Face Space!")

# Display available API endpoints and parameters
client.view_api()
