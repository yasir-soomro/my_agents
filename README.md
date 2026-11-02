# My First Agent

A project assistant that uses a Hugging Face Space to decide when to call the
`get_project_status` tool.

## Setup

1. Copy `.env.example` to `.env`.
2. Set `HF_TOKEN` to a Hugging Face access token and `HF_SPACE_ID` to your
   Space ID in `owner/space-name` format.
3. Install dependencies with `uv sync`.
4. Run the agent with `uv run python -m my_first_agent.agent`.

The `.env` file is local configuration and is excluded from Git.