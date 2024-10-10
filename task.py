class Task:
    def __init__(self, title, description, due_date, status="incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_task_completed(self,title):
        self.status = "completed"

    def mark_in_progress(self):
        self.status = "in progress"

    def d_due_date(self, new_due_date):
        self.due_date = new_due_date

    def details(self):
        return {
            "Title": self.title,
            "Description": self.description,
            "Due Date": self.due_date,
            "Status": self.status
        }
