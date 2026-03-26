import json
import os

# --- PERSISTENCE LAYER ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME= os.path.join(BASE_DIR, "tasks_v2.json")

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks,file, indent=4)
        
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

def mark_as_pending(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "pending"
            return True
    return False

def pending_tasks(tasks):
    return [t for t in tasks if t["status"] == "pending"]
def completed_tasks(tasks):
    return [t for t in tasks if t["status"] == "done"]

# --- UI LAYER (The "Face") ---
MENU = """
Add Task              - a
Delete Task           - d
Show Tasks            - s
Mark Tasks as done    - u
Mark Tasks as pending - b
Pending Tasks         - p
Completed Tasks       - c
Exit app              - e
"""
def print_tasks(tasks):
    if not tasks:
        print("-- No tasks found --")
        return
    print("\nID  |         TASKS         | STATUS")
    print("-"*40)
    for task in tasks:
        print(f"{task["id"]:<3} | {task["name"]:<24} | {task["status"]}")
    print("-"*40)
        

# --- MAIN PROGRAM (The "Glue") ---
def main():
    tasks = load_tasks()
    print("-- Welcome to the Task Manager!! --")
    while True:
        print(MENU)
        choice = input("Enter your choice: \n").lower().strip()

        if choice == "a":
            task_name = input("Enter the task name: \n")
            add_new_task(tasks, task_name)
            save_tasks(tasks)
            print("-- Task added succesfuly --")

        elif choice == "s":
            print_tasks(tasks)

        elif choice == "d":
            try:
                task_id = int(input("Enter the task ID: \n"))
                if delete_task(tasks, task_id):
                    save_tasks(tasks)
                    print("-- Task deleted succesfuly --")
                else:
                    print("-- Enter a valid ID --")
            except ValueError:
                print("-- Invalid Format --")

        elif choice == "b":
            try:
                task_id = int(input("Enter the task ID: \n"))
                if mark_as_pending(tasks, task_id):
                    save_tasks(tasks)
                    print("-- Task succesfuly updated --")
                else:
                    print("-- Enter a valid ID --")
            except ValueError:
                print("-- Invalid Format --")


        elif choice == "u":
            try:
                task_id = int(input("Enter the task ID: \n"))
                if mark_as_done(tasks, task_id):
                    save_tasks(tasks)
                    print("-- Task succesfuly updated --")
                else:
                    print("-- Enter a valid ID --")
            except ValueError:
                print("-- Invalid Format --")
        
        elif choice == "p":
            print_tasks(pending_tasks(tasks))

        elif choice == "c":
            print_tasks(completed_tasks(tasks))
            
        elif choice == "e":
            print("-- Goodbye! --")
            break

        else:
            print("-- Invalid choice --")




if __name__ == "__main__":
    main()
