"""Tasks."""


class Task(list):
    """Define the Task class."""

    name = None
    date = None
    time = None
    note = None


class Add_New(Task):
    """Define the Add_New class."""

    def __init__(self):
        """Customize the class init."""
        self.name = input("What is the task? ")
        self.data = input("What is the date? ")