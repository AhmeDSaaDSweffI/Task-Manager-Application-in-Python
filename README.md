<div align="center">

# 📋 Task Manager Application in Python

### A clean, command-line task manager built to demonstrate real-world Object-Oriented Programming in Python.

Create, track, and organize **Personal** and **Work** tasks straight from your terminal — with local JSON persistence so nothing is ever lost between sessions.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-None-blueviolet?style=for-the-badge)

![Samsung Innovation Campus](https://img.shields.io/badge/Samsung%20Innovation%20Campus-1428A0?style=for-the-badge&logo=samsung&logoColor=white)

> 🎓 Developed as part of the **Samsung Innovation Campus** program.

![Task Manager Screenshot](https://github.com/user-attachments/assets/96d7c4a1-2d07-41bd-b292-cf13e90cc23e)

</div>

---

## 📖 About The Project

**Task Manager Application in Python** is a lightweight command-line interface (CLI) tool for managing your daily to-dos. Rather than reaching for a heavyweight framework, it's built from the ground up with pure Python and the standard library — making it a great reference for anyone learning how **Object-Oriented Programming** translates into a working application.

At its core, a single `Task` base class defines shared behavior, while `PersonalTask` and `workTask` **inherit** from it and extend it with their own attributes. This showcases **inheritance** and **polymorphism** in a practical, easy-to-follow way. All your tasks are transparently saved to a local `data.json` file, so your list survives across runs — no database required.

This project was built by a two-person team as part of the **Samsung Innovation Campus** program — a global initiative by Samsung that equips learners with hands-on skills in software development and emerging technologies.

---

## ✨ Features

- 🧩 **Object-Oriented by Design** — A shared `Task` base class with `PersonalTask` and `workTask` subclasses demonstrating **inheritance** and **polymorphism**.
- ➕ **Full Task Lifecycle** — **Create**, **update**, **delete**, and **track** tasks with a simple menu-driven interface.
- 🗂️ **Two Task Types** — Manage **Personal Tasks** (with a `category` like *family*, *sports*, etc.) and **Work Tasks** (with a `priority` of *low*, *medium*, or *high*).
- 🚦 **Status Tracking** — Every task carries a clear status (`incomplete` → `completed`) so you always know what's left.
- 📅 **Due Dates** — Assign and update due dates to keep your schedule on track.
- 💾 **Local JSON Persistence** — Tasks are stored in `data.json`, keeping your data readable, portable, and safe between sessions.
- 🛡️ **Robust Error Handling** — Invalid inputs and empty-list scenarios are handled gracefully instead of crashing.
- 📦 **Zero Dependencies** — Runs on nothing more than a standard Python installation.

---

## 🏗️ Project Structure

The project is organized into clear, single-responsibility modules that reflect its OOP design:

```text
Task-Manager-Application-in-Python/
│
├── main.py           # 🚀 Entry point — runs the interactive CLI menu loop
├── taskManager.py    # 🧠 TaskManager class — add, remove, display & update tasks
├── task.py           # 🧱 Task — the base class (title, description, due date, status)
├── personalTask.py   # 👤 PersonalTask — inherits Task, adds a `category`
├── workTask.py       # 💼 workTask — inherits Task, adds a `priority`
├── data.json         # 💾 Local storage for persisted tasks
└── README.md         # 📖 You are here
```

### 🧬 The Class Hierarchy

```text
              ┌──────────────┐
              │     Task     │   (base class)
              │──────────────│
              │ title        │
              │ description  │
              │ due_date     │
              │ status       │
              └──────┬───────┘
                     │  inherits
        ┌────────────┴────────────┐
        ▼                         ▼
┌────────────────┐        ┌────────────────┐
│  PersonalTask  │        │    workTask    │
│────────────────│        │────────────────│
│ + category     │        │ + priority     │
└────────────────┘        └────────────────┘
```

---

## ✅ Prerequisites

All you need is **Python 3.8 or newer**. The application relies solely on the standard library (`json`), so there are no external packages to install.

Check your Python version with:

```bash
python --version
```

---

## ⚙️ Installation

Get up and running in just a few steps:

**1. Clone the repository**

```bash
git clone https://github.com/your-username/Task-Manager-Application-in-Python.git
```

**2. Navigate into the project directory**

```bash
cd Task-Manager-Application-in-Python
```

**3. Run the application**

```bash
python main.py
```

> 💡 On some systems you may need to use `python3` instead of `python`.

---

## 🚀 Usage

Once launched, you'll be greeted by an interactive menu. Simply enter the number that matches the action you'd like to perform:

```text
Task Manager
1. Add Task
2. Delete Task
3. Show List of Tasks
4. Update Task Due Date
5. Mark Task as Completed
6. Save and Quit

Enter your choice:
```

### 🔧 What each option does

| Option | Action | Description |
| :----: | :----- | :---------- |
| **1** | ➕ **Add Task** | Create a new task — choose `personal` or `work`, then enter the title, description, and due date (plus a category or priority). |
| **2** | 🗑️ **Delete Task** | Remove a task from your list by its title. |
| **3** | 📋 **Show List of Tasks** | Display all currently stored tasks. |
| **4** | 📅 **Update Task Due Date** | Change the due date of an existing task. |
| **5** | ✔️ **Mark Task as Completed** | Flip a task's status to `completed`. |
| **6** | 💾 **Save and Quit** | Persist all changes to `data.json` and exit safely. |

### 📝 Example: Adding a Work Task

```text
Enter your choice: 1
Enter task type (personal/work): work
Enter title: Finish quarterly report
Enter description: Compile Q3 sales figures and charts
Enter due date (YYYY-MM-DD): 2026-07-20
Enter priority (low, medium, high): high
```

---

## 🔮 Future Enhancements

This project is a living learning platform — here are some ideas on the roadmap:

- [ ] 🔍 Search and filter tasks by status, category, or priority.
- [ ] 📊 Sort tasks by due date or priority.
- [ ] ⏰ Overdue-task highlighting and reminders.
- [ ] 🎨 A richer, color-coded terminal UI.
- [ ] 🧪 A unit test suite for the core classes.
- [ ] 🌐 An optional web or GUI front-end.

---

## 🤝 Contributing

Contributions are what make the open-source community such an incredible place to learn and build. **Any contributions you make are greatly appreciated!**

If you have a suggestion that would make this better, please fork the repo and open a pull request. You can also simply open an issue with the tag `enhancement`.

1. **Fork** the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the Branch (`git push origin feature/AmazingFeature`)
5. Open a **Pull Request**

Don't forget to give the project a ⭐ if you found it useful!

---

## 👥 Team

This project was proudly built by a two-person team during the **Samsung Innovation Campus** program:

| Member | Connect |
| :----- | :------ |
| **Alaa Ashraf Abd Elkreem** | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alaa-ashraf-abd-elkreem/) |
| **Ahmed Saad Sweffi** | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahmed-saad-sweffi-09b2751a9) |

---

## 🙏 Acknowledgments

- 🎓 **[Samsung Innovation Campus](https://www.samsung.com/global/sic/)** — for the training, mentorship, and platform that made this project possible.

---

## 📄 License

Distributed under the **MIT License**. See the `LICENSE` file for more information.

---

<div align="center">

Made with ❤️ and 🐍 Python — as part of the **Samsung Innovation Campus** 🎓

</div>
