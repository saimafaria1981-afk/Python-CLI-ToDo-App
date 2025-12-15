# Python CLI Todo App

**Author:** Faria Mahmood 

---

## Overview
This is a **command-line Todo List application** built in Python.  
The app allows users to manage their daily tasks directly in the terminal, making it simple and easy to use.

---

### Core Features
- **Add Task:** Add a new task with a name and priority.  
- **List Tasks:** View all tasks in a **clean table format** with ID, name, status, and priority.  
- **Update Task:** Edit the title of an existing task.  
- **Delete Task:** Remove a task from the list with **confirmation before deletion**.  
- **Mark Complete / Toggle Status:** Toggle task status between `DONE` and `TO DO`.    

### Bonus Features
- **Task Priority:** Assign `Low`, `Medium`, or `High` priority to tasks.  
- **Confirmation Before Deleting:** Prevent accidental deletion.  
- **File-Based Storage (JSON):**  
  - Tasks are automatically saved to `tasks.json` whenever a task is added, updated, deleted, or marked complete.  
  - Tasks are **loaded from JSON** when the app starts, so data persists across runs.  
- **Clean Table Format:** Tasks are displayed in a neat table for easy reading.

---

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the project folder.
3. Run the application using:
python main.py

---

## How Gemini CLI Was Used

Gemini CLI helped generate the initial structure and menu design for the app.
I then modified, debugged, and extended the code to include features like:

-JSON file saving
-Task priority
-Confirmation before deletion
-Toggle complete

---

## Future Improvements

-Due dates
-Add filtering by priority/status
-Implement colored output for status and priority
-Allow sorting tasks by completion or priority

