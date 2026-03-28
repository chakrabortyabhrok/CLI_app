# 🧠 TaskMaster CLI

**A clean, object-oriented Command-Line Task Manager built in Python**

Track your daily tasks with full CRUD support, status updates, and persistent JSON storage.  
Perfect learning project that demonstrates proper OOP principles, separation of concerns, and clean file handling.

---

## ✨ Features

- ➕ **Add new tasks** (auto-generated unique IDs)
- ❌ **Delete tasks** by ID
- 📋 **View all tasks** in a clean table format
- ✅ **Mark tasks as Done**
- 🔄 **Mark tasks as Pending** (undo)
- 📌 **Filter views**:
  - Show only Pending tasks
  - Show only Completed tasks
- 💾 **Automatic persistence** – all tasks are saved to `tasks.json` and survive restarts
- 🛡️ **Safe error handling** for invalid input and corrupted files
- 🏗️ **Well-structured OOP design** (Task class + TaskManager class)

---

## 🛠️ Tech Stack

- **Python 3.8+**
- Pure standard library (no external dependencies)
- `json` for data persistence
- `os` for cross-platform file paths
- Object-Oriented Programming (classes, encapsulation, methods)

---

## 🚀 Quick Start

### 1. Clone or download the project
```bash
git clone https://github.com/yourusername/taskmaster-cli.git
cd taskmaster-cli
