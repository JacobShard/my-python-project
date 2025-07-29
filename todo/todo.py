# Simple To-Do List App

FILENAME = "tasks.txt"  # File to save/load tasks
tasks = []  # This list will store all the to-do items


def load_tasks():
    """Load tasks from the file into the list (if file exists)"""
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        pass  # It's okay if the file doesn't exist yet


def save_tasks():
    """Save the current list of tasks to the file"""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")


def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print(f"'{task}' has been added to your list.")


def remove_task():
    if not tasks:
        print("Your to-do list is empty. Nothing to remove.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks()
            print(f"'{removed}' has been removed from your list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main program loop
load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1–4.")

    input("Press Enter to continue...")
