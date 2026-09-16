from .task import Task
from .storage import load_tasks
from .storage import save_tasks

class TodoList:
    """ Manage a collection of tasks"""

    def __init__(self) :
        self.tasks: list[Task] = [Task.from_dict(data) for data in load_tasks()]

    def add(self, task: Task) -> None:
        if self.tasks:
            task.id = max(item.id for item in self.tasks) + 1
        else:
            task.id = 1
            
        self.tasks.append(task)
        save_tasks(self.tasks)


    def delete(self, task: Task) -> None:
        self.tasks.remove(task)
        save_tasks(self.tasks)


    def done(self, task: Task) -> None:
        task.status = "done"
        save_tasks(self.tasks)

    def edit(self, task: Task, title: str | None = None, status: str | None = None) -> None:
        if title is not None:
            task.title = title

        if status is not None:
            task.status = status

        save_tasks(self.tasks)


    def list(self) -> list[Task]:
        return self.tasks

