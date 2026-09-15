from utils.task import Task
from utils.todo_list import TodoList

todo_list = TodoList()

task = Task(1, "Learn OOP", "todo")

todo_list.add(task)

print(todo_list.list())

todo_list.done(task)

print(task.status)

todo_list.delete(task)

print(todo_list.list())