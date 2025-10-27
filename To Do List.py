import json
import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama for Windows/IDLE support
init(autoreset=True)

# File where tasks will be saved
TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "completed": self.completed
        }

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**task) for task in data]
        else:
            self.tasks = []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title, due_date=None):
        task = Task(title, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print(Fore.GREEN + f"✔ Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks found.")
            return

        print(Fore.CYAN + "\nYour Tasks:")
        for i, task in enumerate(self.tasks, 1):
            status = Fore.GREEN + "[✓]" if task.completed else Fore.RED + "[ ]"
            due = f" (Due: {task.due_date})" if task.due_date else ""
            print(f"{i}. {status} {task.title}{due}")
        print()

    def mark_completed(self, index):
        try:
            self.tasks[index - 1].completed = True
            self.save_tasks()
            print(Fore.GREEN + "Task marked as completed!")
        except IndexError:
            print(Fore.RED + "Invalid task number!")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(Fore.YELLOW + f"🗑️  Task '{removed.title}' deleted.")
        except IndexError:
            print(Fore.RED + "Invalid task number!")

    def upcoming_tasks(self):
        print(Fore.CYAN + "\nUpcoming Tasks (with due dates):")
        now = datetime.now()
        found = False
        for task in self.tasks:
            if task.due_date:
                due = datetime.strptime(task.due_date, "%Y-%m-%d")
                if due > now and not task.completed:
                    print(Fore.MAGENTA + f"- {task.title} (Due: {task.due_date})")
                    found = True
        if not found:
            print(Fore.YELLOW + "No upcoming tasks.")

def main():
    todo = ToDoList()
    while True:
        print(Style.BRIGHT + Fore.BLUE + "\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. View Upcoming Tasks")
        print("6. Exit")

        choice = input(Fore.CYAN + "Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            todo.add_task(title, due_date if due_date else None)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter task number to mark completed: "))
            todo.mark_completed(index)

        elif choice == "4":
            todo.view_tasks()
            index = int(input("Enter task number to delete: "))
            todo.delete_task(index)

        elif choice == "5":
            todo.upcoming_tasks()

        elif choice == "6":
            print(Fore.GREEN + "Goodbye! Your tasks are saved.")
            break

        else:
            print(Fore.RED + "Invalid choice! Try again.")

if __name__ == "__main__":
    main()
