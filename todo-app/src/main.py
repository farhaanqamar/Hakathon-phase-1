from todo_manager import TodoManager

def display_menu():
    print("\n--- Todo App Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("-----------------------")

def add_task_cli(manager):
    title = input("Enter task title: ").strip()
    description = input("Enter task description (optional): ").strip()
    task, error = manager.add_task(title, description)
    if error:
        print(f"Error: {error}")
    else:
        print(f"Task \"{task['title']}\" added with ID: {task['id']}.")

def view_tasks_cli(manager):
    tasks = manager.get_all_tasks()
    if not tasks:
        print("No tasks to display.")
        return

    print("\n--- Your Tasks ---")
    print(f"{"ID":<4} | {"Title":<25} | {"Description":<40} | {"Status":<10}")
    print("-" * 85)
    for task in tasks:
        title = task['title'] if len(task['title']) <= 25 else task['title'][:22] + "..."
        description = task['description'] if len(task['description']) <= 40 else task['description'][:37] + "..."
        print(f"{task['id']:<4} | {title:<25} | {description:<40} | {task['status']:<10}")
    print("-------------------")

def update_task_cli(manager):
    try:
        task_id = int(input("Enter the ID of the task to update: "))
    except ValueError:
        print("Invalid input. Please enter a number for the task ID.")
        return

    new_title = input("Enter new title (leave blank to keep current): ").strip()
    new_description = input("Enter new description (leave blank to keep current): ").strip()

    if not new_title and not new_description:
        print(f"No changes specified for task {task_id}.")
        return
    
    # Pass None if input is blank to signify no change, empty string if user explicitly wants to clear
    title_to_pass = new_title if new_title != "" else None
    description_to_pass = new_description if new_description != "" else None

    updated, error = manager.update_task(task_id, title_to_pass, description_to_pass)
    if error:
        print(f"Error: {error}")
    elif updated:
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"No changes made to task {task_id}.") # Should not happen if updated is False and no error

def delete_task_cli(manager):
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number for the task ID.")
        return

    deleted, error = manager.delete_task(task_id)
    if error:
        print(f"Error: {error}")
    else:
        print(f"Task {task_id} deleted successfully.")

def mark_task_status_cli(manager):
    try:
        task_id = int(input("Enter the ID of the task to mark: "))
    except ValueError:
        print("Invalid input. Please enter a number for the task ID.")
        return
    
    status_input = input("Mark as complete? (yes/no): ").strip().lower()
    if status_input not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
    
    is_complete = (status_input == "yes")

    marked, error = manager.mark_task_status(task_id, is_complete)
    if error:
        print(f"Error: {error}")
    else:
        status_text = "Complete" if is_complete else "Pending"
        print(f"Task {task_id} marked as {status_text} successfully.")

def main():
    manager = TodoManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_task_cli(manager)
        elif choice == '2':
            view_tasks_cli(manager)
        elif choice == '3':
            update_task_cli(manager)
        elif choice == '4':
            delete_task_cli(manager)
        elif choice == '5':
            mark_task_status_cli(manager)
        elif choice == '6':
            print("Exiting Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
