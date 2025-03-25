tasks = []

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print(f"Added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks in the list!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['task']}")

def mark_done():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
                print(f"Marked '{tasks[num]['task']}' as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice based on Your Need (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
