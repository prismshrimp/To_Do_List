def load_tasks(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            tasks = [line.strip() for line in file if line.strip()]
    return tasks

def save_tasks(tasks, file_path):
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("======================")

def add_task(tasks, file_path):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks, file_path)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list!")
    else:
        print("\n=== Your Tasks ===")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
        print("==================")

def update_task(tasks, file_path):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to update: ")) - 1
            if 0 <= index < len(tasks):
                new_task = input("Enter the new task description: ").strip()
                if new_task:
                    tasks[index] = new_task
                    save_tasks(tasks, file_path)
                    print(f"Task {index + 1} updated successfully!")
                else:
                    print("New task description cannot be empty!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task(tasks, file_path):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                save_tasks(tasks, file_path)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    file_path = "../data/tasks.txt"  # Relative path to data folder
    tasks = load_tasks(file_path)
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_task(tasks, file_path)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks, file_path)
        elif choice == '4':
            delete_task(tasks, file_path)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()