import json
import os
from tasks import Tasks

class TaskManager:

    def __init__(self):
        self._tasks = []
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.file_name= os.path.join(BASE_DIR, "tasks.json")

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            print("-- File not found --\n")
            return
        
        try:
            with open(self.file_name, "r") as file:
                raw_data = json.load(file)
            if isinstance(raw_data, list):
                    tasks_data = raw_data

            else:
                raise ValueError("-- Invalid JSON Format --")
            
            self._tasks = []

            for t in tasks_data:
                new_obj = Tasks(
                    id=t["id"],
                    name=t["name"],
                    status=t["status"]
                )
                self._tasks.append(new_obj)
                print(f"Loaded: {len(self._tasks)} tasks")
        
        except Exception as e:
            print(f"Error Loading: {e}")
    
    def save_tasks(self):
        data = [task.to_dict() for task in self._tasks]
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)
        
    def get_new_id(self):
        if not self._tasks:
            return 1
        else:
            return max(task.id for task in self._tasks ) + 1
    
    def add_new_task(self, new_task):
        self._tasks.append(new_task)
        self.save_tasks()

    def delete_task(self, task_id):
        for task in self._tasks:
            if task["id"] == task_id:
                self._tasks.remove(task)
                return True
        return False
        
    def mark_as_done(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                task.status = "done"
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

    def print_tasks(self):
        if not self._tasks:
            print("-- No tasks found --")
            return
        print("\nID  |           TASKS          | STATUS")
        print("-"*40)
        for task in self._tasks:
            print(task.display_row())
        print("-"*40)
        
