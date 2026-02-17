import json
import os

# --- PERSISTENCE LAYER ---

# This bit of magic finds the exact folder where THIS script is saved.
# No matter where you run the terminal from, it will look in the script's folder.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")

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
        json.dump(tasks, file, indent=4)

# --- LOGIC LAYER (The "Brain") ---

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(tasks, name):
    new_task = {
        "id": get_next_id(tasks),
        "name": name,
        "status": "pending"
    }
    tasks.append(new_task)

def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False

def mark_done(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            return True
    return False

def list_pending(tasks):
    return [t for t in tasks if t["status"] == "pending"]

def list_completed(tasks):
    return [t for t in tasks if t["status"] == "done"]

# --- UI LAYER (The "Face") ---

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
        print("\n--- No tasks found. ---")
        return
    print("\nID  | Task Name                | Status")
    print("-" * 40)
    for t in tasks:
        # This formatting makes columns line up nicely
        print(f"{t['id']: <3} | {t['name']: <24} | {t['status']}")
    print("-" * 40)

# --- MAIN PROGRAM (The "Glue") ---

def main():
    tasks = load_tasks()
    print("Welcome to Task Manager V2!")

    while True:
        print(MENU)
        choice = input("Enter choice: ").lower().strip()

        if choice == "a":
            name = input("Task name: ")
            add_task(tasks, name)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "s":
            print_tasks(tasks)

        elif choice == "d":
            try:
                task_id = int(input("Enter ID to delete: "))
                if delete_task(tasks, task_id):
                    save_tasks(tasks)
                    print("Deleted successfully.")
                else:
                    print("ID not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "u":
            try:
                task_id = int(input("Enter ID to mark as done: "))
                if mark_done(tasks, task_id):
                    save_tasks(tasks)
                    print("Updated successfully.")
                else:
                    print("ID not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "p":
            print_tasks(list_pending(tasks))

        elif choice == "c":
            print_tasks(list_completed(tasks))

        elif choice == "e":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

# The Entry Point: This "turns the key" to start the engine
if __name__ == "__main__":
    main()