import argparse

from utils.task import Task
from utils.todo_list import TodoList

def find_task(todo_list: TodoList, task_id: int) -> Task | None:
    for task in todo_list.list():
        if task.id == task_id:
            return task
        return None

def main() -> None:
    parser = argparse.ArgumentParser(description="Todo List CLI")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    edit_parser = subparsers.add_parser("edit")
    edit_parser.add_argument("id", type=int)
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--status")

    args = parser.parse_args()

    todo_list = TodoList()

    if args.command == "add":
        task = Task(0, args.title, "todo")
        todo_list.add(task)
        print(f"Task added with ID: {task.id}")

    elif args.command == "list":
        tasks = todo_list.list()

        for task in tasks:
            print(f"{task.id}. {task.title} - "f"{task.status} - {task.created_at}"
)

    elif args.command == "done":
        task = find_task(todo_list, args.id)

        if task:
            todo_list.done(task)
            print(f"Task {task.id} marked as done.")

    elif args.command == "delete":
        task = find_task(todo_list, args.id)

        if task:
            todo_list.delete(task)
            print(f"Task {task.id} deleted.")

    elif args.command == "edit":
        task = find_task(todo_list, args.id)

        if task:
            todo_list.edit(
            task,
            title=args.title,
            status=args.status,
)
            print(f"Task {task.id} updated.")

if __name__ == "__main__":
    main()