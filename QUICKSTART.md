markdown
# Quickstart

## 1. Create a Virtual Environment

```powershell
python -m venv .venv

2. Activate the Virtual Environment
venv\Scripts\Activate.ps1

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
Add a Task
python main.py add "Learning OOP"
List Tasks
python main.py list
Mark a Task as Done
python main.py done 1
Edit a Task
python main.py edit 1 --title "Learning Python OOP"
Delete a Task
python main.py delete 1

5. Filter Tasks
Show Todo Tasks
python main.py list --status todo
Show Completed Tasks
python main.py list --status done