import json
from taskManager import TaskManager
from task import Task
from personalTask import PersonalTask
from workTask import workTask

# Load data from the JSON file
with open("data.json", "r") as file:
    data = json.load(file)


def save_data():
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show List of Tasks")
        print("4. Update Task Due Date")
        print("5. Mark Task as Completed")
        print("6. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_type = input("Enter task type (personal/work): ").strip().lower()
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            if task_type == "personal":
                category = input("Enter category (family, sports, etc.): ")
                new_task = PersonalTask(title, description, due_date, category=category)
            elif task_type == "work":
                priority = input("Enter priority (low, medium, high): ")
                new_task = workTask(title, description, due_date, priority=priority)
            else:
                print("Invalid task type.")
                continue  # Skip invalid task type

            manager.add_task(new_task)
            data.append(new_task.details())

        elif choice == "2":
            try:
                if not manager.tasks:
                    print("The task list is empty.")
                    continue
                title = input("Enter the title of the task to delete: ")
                manager.remove_task(title)
                save_data()
            except Exception as e:
                print(e)

        elif choice == "3":
            manager.display_tasks(data)

        elif choice == "4":
            title = input("Enter the title of the task to update: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            manager.update_due_date(title, new_due_date)

        elif choice == "5":
            title = input("Enter the title of the task to mark as completed: ")
            if manager.mark_completed(title):
                for task in data:
                    if task["Title"] == title:
                        task["Status"] = "complete"
                        break
                save_data()

        elif choice == "6":
            save_data()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
