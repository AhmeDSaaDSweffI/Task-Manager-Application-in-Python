from task import Task
class PersonalTask(Task):
    def __init__(self, title, description, due_date, status="incomplete", category=None):
        super().__init__(title, description, due_date, status)
        self.category = category

    def _show2_(self):
        return f"PersonalTask[ Title = {self.title}, description = {self.description} , Due Date = {self.due_date}, Status = {self.status}, Category = {self.category}]"

    def task_info(self):
        return f" Category: {self.category}"