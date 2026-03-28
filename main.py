from tasks import Tasks
from manager import TaskManager

def main():
    manager = TaskManager()
    manager.load_tasks()

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
    print("-- Welcome to the Task Manager!! --")
    while True:
        print(MENU)
        choice = input("Enter your choice: \n").lower().strip()

        if choice == "a":
            task_name = input("Enter the task name: \n")
            new_id = manager.get_new_id()
            status = "pending"
            new_task = Tasks(new_id,task_name, status)
            manager.add_new_task(new_task)
            print("-- Task added succesfuly --")

        elif choice == "s":
            manager.print_tasks()

        elif choice == "d":
            try:
                task_id = int(input("Enter the task ID: \n"))
                if manager.delete_task(task_id):
                    manager.save_tasks()
                    print("-- Task deleted succesfuly --")
                else:
                    print("-- Enter a valid ID --")
            except ValueError:
                print("-- Invalid Format --")

        elif choice == "b":
            try:
                task_id = int(input("Enter the task ID: \n"))
                if manager.mark_as_pending(task_id):
                    manager.save_tasks()
                    print("-- Task succesfuly updated --")
                else:
                    print("-- Enter a valid ID --")
            except ValueError:
                print("-- Invalid Format --")


        elif choice == "u":
            try:
                task_id = int(input("Enter the task ID: \n"))
                if manager.mark_as_done(task_id):
                    manager.save_tasks()
                    print("-- Task succesfuly updated --")
                else:
                    print("-- Enter a valid ID --")
            except ValueError:
                print("-- Invalid Format --")
        
        elif choice == "p":
            manager.print_tasks(manager.pending_tasks())

        elif choice == "c":
            manager.print_tasks(manager.completed_tasks())
            
        elif choice == "e":
            print("-- Goodbye! --")
            break

        else:
            print("-- Invalid choice --")


if __name__ == "__main__":
    main()
