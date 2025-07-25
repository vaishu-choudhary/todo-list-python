# To-Do List App

# File name to store tasks
FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = f.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("❌ No tasks found!")

    else:
        print("📝\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("========== 📝 TO-DO LIST ==========")

        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Save & Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            print("Task added!\n")

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f"Removed: {removed}\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a number.\n")

        elif choice == "4":
            save_tasks(tasks)
            print("✅ Tasks saved. Goodbye!")

            break

        else:
            print("Invalid choice. Try again.\n")

# Run the app
if __name__ == "__main__":
    main()
