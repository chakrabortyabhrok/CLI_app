tasks = [
    {
        "id": 1,
        "name": "Take a walk",
        "status": "pending"
    },
    {
        "id": 2,
        "name": "Practice guitar",
        "status": "done"
    },
    {
        "id": 3,
        "name": "Read a book",
        "status": "pending"
    },
    {
        "id": 4,
        "name": "Call a freind",
        "status": "done"
    }
]

print("ID |       TASKS NAME       | STATUS")
print("-" * 40)
for task in tasks:
    print(f"{task["id"]: < 3} {task["name"]: <24} {task["status"]}")
print("-" * 40)
