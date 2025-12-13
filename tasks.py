# A list to store tasks
tasks = []

def add_task():
    """Adds a new task to the list."""
    task_name = input("Enter the task name: ")
    
    if not task_name:
        print("Task name cannot be empty.")
        return
    
    priority = input("Enter the task priority (Low, Medium, High): ")
    
    max_id = 0
    for task in tasks:
        if task ['id'] > max_id:
            max_id = task['id']
    new_id = max_id + 1
        
    tasks.append({"id": new_id, "name": task_name, "completed": False , "priority" : priority})
    print(f"Task '{task_name}' with ID '{new_id}' added successfully!")

def list_tasks():
    """Lists all the tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- Your Tasks ---")
        for task in tasks:
            status = "DONE" if task["completed"] else "TO DO"
            print(f"ID: {task['id']} {task['name']} [{status}] (Priority: {task['priority']})")

def mark_task():
    """Marks a task as complete."""
    list_tasks()
    if not tasks:
        return

    task_id_input = input("Enter the ID of the task to mark as complete: ")
    
    try:
        task_id = int(task_id_input)
    except ValueError:
        print(f"Invalid ID '{task_id_input}'. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task with ID '{task_id}' marked as complete!")
            return
            
    print(f"Task with ID '{task_id}' not found.")

def update_task():
    """Updates the title of an existing task."""
    if not tasks:
        print("No tasks to update.")
        return

    list_tasks()

    task_id = input("Enter task ID to update: ")

    for task in tasks:
        if (task["id"]) == task_id:
            print(f'Current title: "{task["name"]}"')

            new_title = input("Enter new title or leave blank to keep same: ")

            if new_title:
                task["name"] = new_title
                print(f"Task '{task['name']}' with ID '{task_id}' updated successfully!")
            else:
                print("Task unchanged.")

            return

    print("Task with ID '{task_id}' not found.")


def delete_task():
    """Deletes a task from the list."""
    list_tasks()
    if not tasks:
        return

    task_id_input = input("Enter the ID of the task to delete: ")

    try:
        task_id = int(task_id_input)
    except ValueError:
        print(f"Invalid ID '{task_id_input}'. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            confirm = input(f"Are you sure you want to delete task '{task['name']}'? (y/n): ")
           
            if confirm.lower() =='y':
                tasks.remove(task)
                print(f"Task '{task['name']}' with ID '{task_id}' deleted successfully!")
            else:
                print("Deletion of Task {task_id} cancelled.")

            return
            
    print(f"Task with ID '{task_id}' not found.")
