import json
import os

#Persistence Layer: Saving and Loading Data from Files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks_v2.json")

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open (FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def save_tasks(tasks):
    with open (FILE_NAME, "w") as file:
        json.dump(tasks, file, indent = 4)
    
#Logic Layer: The "Brain" – Manipulating Tasks
def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_tasks(tasks, task_name):
    new_task = {
        "id":get_next_id(tasks),
        "name": task_name,
        "status": "pending"
    }
    tasks.append(new_task)

def delete_tasks(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False

def mark_as_done(tasks, task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            return True
        else:
            print("Enter a valid ID..\n")
            return False
    return False

def pending_tasks(tasks):
    return[t for t in tasks if t["status"] == "pending"]

def complete_tasks(tasks):
    return[t for t in tasks if t["status"] == "done"]


#UI Layer: The "Face" – Interacting with the User
MENU = """
Add Task        - a
Show All Tasks  - s
Delete Task     - d
Mark Done       - u
Pending Tasks   - p
Completed Tasks - c
Exit            - e
"""

def print_tasks(tasks):
    if not tasks:
        print("\n--NO_TASKS_FOUND--")
        return
    print("\nID  |        TASK NAME        | STATUS")
    print("-" * 40)
    for t in tasks:
        print(f"{t["id"]: <3} | {t["name"]: <24} | {t["status"]}")
    print("-" * 40)
        
def main():
    tasks = load_tasks()
    print("Welcome to Task Manager V2!\n")

    while True:
        print(MENU)
        choice = input("Enter choice: \n").lower().strip()

        if choice == "a":
            task_name = input("Enter Task name: \n")
            add_tasks(tasks, task_name)
            save_tasks(tasks)
            print("Task Added. ")

        elif choice == "s":
            print_tasks(tasks)

        elif choice == "d":
            try:
                task_id = int(input("Enter the ID you want to delete: \n"))
                if delete_tasks(tasks, task_id):
                    save_tasks(tasks)
                    print("Task Deleted. \n")
            except ValueError:
                print("Enter a valid ID.. \n")

        elif choice == "u":
            try:
                task_id = int(input("Enter the Taks ID:\n"))
                if mark_as_done(tasks, task_id):
                    save_tasks(tasks)
                    print("Task marked as done.\n")
            except ValueError:
                print("Enter a valid ID ..\n")

        elif choice == "p":
            print_tasks(pending_tasks(tasks))
            

        elif choice == "c":
            print_tasks(complete_tasks(tasks))

        elif choice == "e":
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice..\n")

if __name__ == "__main__":
    main()


#do the save_tasks and new_id 3 times, after understanding only.
#complete this layer full
