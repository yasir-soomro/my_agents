import os
from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()

token = os.getenv("HF_TOKEN")
SPACE_ID = os.getenv("HF_SPACE_ID")

if not token:
    raise ValueError("HF_TOKEN missing")

if not SPACE_ID:
    raise ValueError("HF_SPACE_ID missing")

api = HfApi(token=token)

# Check Space runtime
runtime = api.get_space_runtime(repo_id=SPACE_ID)

print("\n===== SPACE RUNTIME =====")
print("Stage:", runtime.stage)
print("Hardware:", runtime.hardware)
print("Requested hardware:", runtime.requested_hardware)


# Check application logs
print("\n===== RUNTIME LOGS =====")

try:
    logs = list(api.fetch_space_logs(repo_id=SPACE_ID))

    if logs:
        for line in logs[-40:]:
            print(line, end="")

    else:
        print("No runtime logs returned.")

except Exception as error:
    print("Could not retrieve runtime logs:", error)


# Check build logs
print("\n===== BUILD LOGS =====")

try:
    logs = list(
        api.fetch_space_logs(
            repo_id=SPACE_ID,
            build=True,
        )
    )

    for line in logs[-30:]:
        print(line, end="")

except Exception as error:
    print("Could not retrieve build logs:", error)