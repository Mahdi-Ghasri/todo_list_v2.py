from utils.task import Task
from utils.todo_list import TodoList

todo_list = TodoList()

task = Task(0, "Learn OOP", "todo")

todo_list.add(task)

print(task.id)

todo_list.done(task)

print(task.status)

todo_list.delete(task)

print(todo_list.list())