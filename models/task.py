class Task:
    """
    Represents a task inside a project.
    """

    def __init__(self, title, assigned_to, status="Incomplete"):
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def to_dict(self):
        return {
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }

    def __str__(self):
        return f"{self.title} - {self.status}"