tasks = []

def display_menu():
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

def update_task():
    view_tasks()
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_number] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
