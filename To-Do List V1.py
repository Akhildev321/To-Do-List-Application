FILENAME = "tasks.txt"

# Load existing tasks
try:
    with open(FILENAME, "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("\nNo tasks yet.")
    
    elif choice == "2":
        new_task = input("Enter the new task: ").strip()
        if new_task:
            tasks.append(new_task)
            print("Task added.")
        else:
            print("Cannot add an empty task.")
    
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
            continue

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "4":
        # Save tasks before exiting
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
