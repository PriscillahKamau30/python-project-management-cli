class User:
    """
    Represents a user in the system.
    A user can have multiple projects.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]
        }

    def __str__(self):
        return f"{self.name} ({self.email})"