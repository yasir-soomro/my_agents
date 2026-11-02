

def get_project_status(project_name: str) -> str:
    """Return the current status of a project."""

    projects = {
        "ClientPilot": "In progress",
        "ChatME": "Planning",
    }

    return projects.get(project_name, "Project not found")


if __name__ == "__main__":
    result = get_project_status("ClientPilot")
    print(result)
