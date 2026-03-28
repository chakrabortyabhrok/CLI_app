import json
import os
from tasks import Tasks

class TaskManager:

    def __init__(self):
        self._tasks = []
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(BASE_DIR, "tasks.json")

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
            return max(task.id for task in self._tasks) + 1
    
    def add_new_task(self, new_task):
        self._tasks.append(new_task)
        self.save_tasks()

    def delete_task(self, task_id):
        for task in self._tasks[:]:
            if task.id == task_id:
                self._tasks.remove(task)
                return True
        return False
        
    def mark_as_done(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                task.status = "done"
                return True
        return False

    def mark_as_pending(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                task.status = "pending"
                return True
        return False

    def pending_tasks(self):
        return [t for t in self._tasks if t.status == "pending"]

    def completed_tasks(self):
        return [t for t in self._tasks if t.status == "done"]

    def print_tasks(self, task_list):
        if not task_list:
            print("-- No tasks found --")
            return
        
        print("\nID  |           TASKS          | STATUS")
        print("-" * 40)
        for task in task_list:
            print(task.display_row())
        print("-" * 40)


    def print_specific_tasks(self, user_demand):
        if user_demand == "p":
            self.print_tasks(self.pending_tasks())
        elif user_demand == "c":
            self.print_tasks(self.completed_tasks())
        else:
            print("-- Invalid filter choice --")