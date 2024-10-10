from task import Task
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' has been removed.")
                return
        print(f"No task found with the title '{title}'.")

    def display_tasks(self,data):
        for task in data:
            print(task)
            if not data:
                print("No tasks available.")

    def mark_completed(self,title):
        for task in self.tasks:
            if task["Title"]==title:
                task.mark_task_completed(title)
                print(f"task '{title}' marked as completed.")
                return True
            print("invalid title")

    def update_due_date(self, title, new_due_date):
        for task in self.tasks:
            if task.title == title:
                task.d_due_date(new_due_date)
                print(f"Task '{title}' due date updated to {new_due_date}")
                return
        print("Invalid title")