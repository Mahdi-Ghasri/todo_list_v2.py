import json

def save_tasks(tasks: list[dict]) -> None:

    with open("data/tasks.json", "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def load_tasks() -> list[dict]:

    try:
        with open("data/tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


    