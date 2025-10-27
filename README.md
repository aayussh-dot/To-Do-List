Advanced To-Do List App (Python)

An advanced, terminal-based To-Do List Manager built with Python, featuring OOP, JSON file storage, due date tracking, and colored CLI output using colorama.
Perfect for organizing daily tasks — and showcasing your Python skills!

🚀 Features

✅ Add, view, complete, and delete tasks
✅ Persistent storage — tasks are saved automatically in tasks.json
✅ Upcoming task tracker using Python’s datetime
✅ Beautiful colored terminal UI using colorama
✅ Robust error handling and modular OOP design

🧩 Tech Stack

Python 3.x

colorama (for colored CLI)

json (for data storage)

datetime (for due dates)

OOP principles

📂 Project Structure
advanced_todo/
│
├── todo_advanced.py      # Main program file
├── tasks.json            # Auto-created storage file
└── README.md             # Project documentation

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/<your-username>/advanced-todo-list.git
cd advanced-todo-list


Install dependencies

pip install colorama


Run the program

python todo_advanced.py

🧠 How It Works

Each task is stored as an object in JSON format.

Due dates are handled using Python’s datetime module.

The program automatically loads and saves tasks between sessions.

The color-coded UI helps differentiate completed and pending tasks.

🎯 Example Output
===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. View Upcoming Tasks
6. Exit

Enter your choice: 1
Enter task title: Finish OS Assignment
Enter due date (YYYY-MM-DD): 2025-10-30
✔ Task 'Finish OS Assignment' added successfully!

🧑‍💻 Author

Ayush Das
🎓 CSE Student at SRM University, Kattankulathur
💻 Passionate about Python, AI, and Automation

🌟 Future Improvements

Add a GUI version using Tkinter or PyQt5

Add a notification/reminder system

Sync with a database or cloud storage

Export tasks as CSV or PDF

📜 License

This project is licensed under the MIT License — feel free to use, modify, and share!
