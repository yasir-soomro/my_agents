
import os

from dotenv import load_dotenv
from gradio_client import Client

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
SPACE_ID = os.getenv("HF_SPACE_ID")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is missing")

if not SPACE_ID:
    raise ValueError("HF_SPACE_ID is missing")

client = Client(
    SPACE_ID,
    token=HF_TOKEN,
)

system_message = """
You are a project assistant.

You have access to this tool:

Tool name: get_project_status

Description:
Returns the current status of a project.

Argument:
project_name (string)

Instructions:

1. Understand the user's request.
2. If project status is requested, select get_project_status.
3. Return exactly one JSON object.
4. Do not execute the tool yourself.
5. Never invent other tools.

For a tool request, return:

{
    "action": "call_tool",
    "tool": "get_project_status",
    "arguments": {
        "project_name": "ClientPilot"
    }
}

For a question that doesn't need a tool, return:

{
    "action": "final_answer",
    "answer": "Your answer here"
}
"""

user_message = "What is the current status of ClientPilot?"

response = client.predict(
    message=user_message,
    system_message=system_message,
    max_tokens=160,
    temperature=0.1,
    top_p=0.9,
    api_name="/respond",
)

print("\n===== USER REQUEST =====")
print(user_message)

print("\n===== QWEN TOOL DECISION =====")
print(response)
