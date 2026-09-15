from task import Task
from storage import load_tasks
from storage import save_tasks

class TodoList:
    """ Manage a collection of tasks"""

    def __init__(self) :
        self.tasks: list[Task] = [Task.from_dict(data) for data in load_tasks()]

    def add(self, task: Task) -> None:
        self.tasks.append(task)

    def delete(self, task: Task) -> None:
        self.tasks.remove(task)

    def done(self, task: Task) -> None:
        task.status = "done"

    def list(self) -> list[Task]:
        return self.tasks

