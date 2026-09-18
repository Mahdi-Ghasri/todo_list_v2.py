# Todo CLI

Expand CLI project

## Description

A simple command-line Todo List application built with Python and Object-Oriented Programming.

The application allows users to create, view, complete, edit, and delete tasks. Tasks are stored in a JSON file so they remain available after the program is closed.

## Features

• Add new tasks
• List all tasks
• Filter tasks by status
• Mark tasks as done
• Edit task title and status
• Delete tasks
• Automatic task ID generation
• Store tasks in JSON format
• Sort tasks by status
• Handle missing or invalid JSON files


## Tech stack

• Python
• Object-Oriented Programming
• argparse
• JSON
• Git & GitHub

Prerequisites

• Python 3.10 or newer
• Git

Installation
Clone the repository and enter the project directory:

bash
git clone <https://github.com/Mahdi-Ghasri/todo_list_v2.py.git>
cd todo_list_v2

Create and activate a virtual environment:

python -m venv venv

Windows PowerShell:
powershell
venv\Scripts\Activate.ps1

Install the required dependencies:
bash
pip install -r requirements.txt

Usage
Add a task
python main.py add "Learn OOP"

List tasks
python main.py list

List only todo tasks
python main.py list --status todo

List completed tasks
python main.py list --status done

Mark a task as done
python main.py done 1

Edit a task
python main.py edit 1 --title "Learn Python OOP"

Change the status:
python main.py edit 1 --status done

Delete a task
python main.py delete 1

Project Structure
todo_list_v2/
│
├── data/
│   └── tasks.json
│
├── utils/
│   ├── __init__.py
│   ├── storage.py
│   ├── task.py
│   └── todo_list.py
│
├── main.py
├── README.md
├── QUICKSTART.md
├── requirements.txt
├── .env.example
└── .gitignore

Data Storage
The storage.py module is responsible for saving and loading task data from the JSON file.

Sorting
Tasks are sorted so that unfinished tasks appear before completed tasks.
Sorting by date is not used as the main sorting method because the Todo List is primarily concerned with task status and task management rather than chronological ordering.

Contributing
This project was created as part of a Python programming course.
Contributions and suggestions are welcome.

License
This project is created for educational purposes.

