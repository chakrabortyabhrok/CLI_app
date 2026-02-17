import json
import os

# --- PERSISTENCE LAYER ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME= os.path.join(BASE_DIR, "tasks_v2.json")

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return[]
    try:
        with open (FILE_NAME, "r"):
            json.load(FILE_NAME)
    except json.JSONDecodeError:
        return[]
    
def save_tasks(tasks):
    with open (FILE_NAME, "w"):
        json.dump(FILE_NAME, tasks, indent=4)
        
# --- LOGIC LAYER (The "Brain") ---
def get_new_id(tasks):
    if not tasks:
        return 1
    else:
        return max(t["id"] for t in tasks ) + 1
    
def add_new_task(tasks, task_name):
    new_task = {
        "id": get_new_id(tasks),
        "name": task_name,
        "status": "pending"
    }
    tasks.append(new_task)

def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False
        
def mark_as_done(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            return True
    return False

def pending_tasks(tasks):
    return [t for t in tasks if t["status"] == "pending"]
def completed_tasks(tasks):
    return [t for t in tasks if t["status"] == "done"]

# --- UI LAYER (The "Face") ---
MENU = """
Add Task        - a
Delete Task     - d
Show Tasks      - s
Update Tasks    - u
Pending Tasks   - p
Completed Tasks - c
Exit app        - e
"""
def print_tasks(tasks):
    if not tasks:
        print("-- No tasks found --")
    print("ID  |         TASKS         | STATUS\n")
    print("-"*40)
    for task in tasks:
        print(f"{task["id"]: < 3} {task["name"]: <24} {task["status"]}")
        print("-"*40)
        return

