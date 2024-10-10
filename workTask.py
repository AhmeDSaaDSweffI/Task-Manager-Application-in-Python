from task import Task


class workTask(Task):
    def __init__(self, title, description, due_date, status="incomplete",priority=None):
        super().__init__(title, description,  due_date)
        self.priority = priority

    def get_type(self):
        return "Work Task"

    def details(self):
        details = super().details()
        details["Priority"] = self.priority
        return details


