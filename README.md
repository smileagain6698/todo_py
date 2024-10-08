
# 📋 Personal To-Do List Application

📝 Description

The Personal To-Do List Application is a simple task management tool built with Python. It allows users to create, view, edit, and delete tasks, and categorize them into groups such as Work, Personal, and Urgent. The tasks are saved locally in a JSON file, ensuring that the task list is preserved across different sessions.

## ✨ Features

- ✅ Task Management: Add tasks with a title, description, and category.
- ✔️ Task Completion & Deletion: Mark tasks as completed or delete them from the     list.
- 🗂️ Task Categorization: Classify tasks into categories such as Work, Personal, or Urgent.
- 💾 Persistence: Tasks are saved locally in a JSON file, allowing them to be available even after the application is closed.


## 📁 Project Structure
``` 
/todo_app
├── todo.py         # Main application logic
├── tasks.json      # JSON file to store tasks
└── README.md       # Project documentation
```
## ⚙️ Installation

1. Clone the repository:


```
git clone https://github.com/smileagain6698/todo_py.git
```
2. Navigate to the project directory:
```
cd todo-app
```
3. Run the application:
- For Command-Line Interface (CLI):
```
 python todo.py
```

## 🏎️ How to Use

🖥️ Command-Line Interface (CLI)
1. Run the application from the terminal:
```
python todo.py
```

2. You will see the following menu:
```
--- To-Do List ---
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit 
```
3. Add a Task:

- Choose option ```1``` and enter the task details when prompted (title, description, category).
4. View Tasks:

- Choose option ```2``` to display all the tasks.
5. Mark a Task as Completed:

- Choose option ```3```, then enter the task number to mark it as completed.
6. Delete a Task:

- Choose option ```4```, then enter the task number to delete it.
7. Exit:
- Choose option ```5``` to exit and save your tasks.
## 🔨 Task Class Structure
The application uses a Task class to handle individual tasks.

``` 
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True
```
## 💾 File Handling
Tasks are saved to and loaded from a ```tasks.json``` file in the following format:

```
[
    {
        "title": "Finish Assignment",
        "description": "Complete the math assignment",
        "category": "Work",
        "completed": false
    },
    ...
]
```
## 🌟 Future Enhancements
- ⏫ Add task priority levels (High, Medium, Low).
- 🔔 Implement reminders and notifications for due tasks.
- 🖼️ Expand the Tkinter GUI to include more interactive elements.

## License

his project is open source and available under the [MIT License](https://choosealicense.com/licenses/mit/).

