from tasks import *
load_tasks()

def display_menu():
    """Displays the main menu."""
    print("\n=== To-Do List Menu ===")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as complete (by Task ID)")
    print("4. Update a task (by Task ID)")
    print("5. Delete a task (by Task ID)")
    print("6. Exit")

def main():
    """Main function to run the To-Do application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            save_tasks()
            print("Exiting the To-Do application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()