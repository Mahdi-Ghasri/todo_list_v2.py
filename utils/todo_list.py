from .task import Task
from .storage import load_tasks
from .storage import save_tasks
class TodoList:
    """Manage a collection of tasks."""


    def __init__(self):
        data = load_tasks()
        self.tasks: list[Task] = [Task.from_dict(item) for item in data]


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


    def list(self, status: str | None = None) -> list[Task]:
        if status == "todo":
            return sorted([task for task in self.tasks if task.status == "todo"]
                          , key = lambda task: task.id)
        if status == "done":
            return sorted([task for task in self.tasks if task.status == "done"],
                          key=lambda task: task.id
                          )
        return sorted(self.tasks, key=lambda task: task.status == "done"
                      )




