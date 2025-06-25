# todo.py

FILENAME = "tasks.txt"

# Load tasks from the file at the start
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print()

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.\n")
    else:
        print("Empty task cannot be added.\n")

# Remove a task by number
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' removed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main menu loop
def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("\nHave a Nice Day!")
            print("📋 Your To-Do List is now a *Ta-Done* List. 😎💼")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
