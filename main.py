import json

class Task:
    def __init__(self, title, description, category, due_date=None):
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} ({self.category}) - {self.due_date if self.due_date else 'No Due Date'}"

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    due_date = due_date if due_date else None
    tasks.append(Task(title, description, category, due_date))
    print("Task added successfully!")

def view_tasks(tasks):
    print("Your Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def mark_task_completed(tasks):
    try:
        index = int(input("Enter task number to mark completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].mark_completed()
            print("Task marked completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def search_tasks(tasks, query):
    results = [task for task in tasks if query.lower() in task.title.lower() or query.lower() in task.description.lower()]
    if results:
        print("Search results:")
        for i, task in enumerate(results):
            print(f"{i+1}. {task}")
    else:
        print("No matching tasks found.")

def main():
    tasks = load_tasks()
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            query = input("Enter search query: ")
            search_tasks(tasks, query)
        elif choice == '6':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()