from models.user import User
from models.project import Project
from models.task import Task


def test_user_creation():
    user = User("Alex", "alex@gmail.com")
    assert user.name == "Alex"


def test_project_add():
    user = User("Alex", "alex@gmail.com")
    project = Project("CLI Tool", "Build tool", "2026-03-01")
    user.add_project(project)
    assert len(user.projects) == 1


def test_task_complete():
    task = Task("Write code", "Alex")
    task.mark_complete()
    assert task.status == "Complete"