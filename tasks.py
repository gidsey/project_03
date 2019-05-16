"""Tasks."""
import datetime

import utilities

fmt = '%d/%m/%Y'


class Task(list):
    """Define the Task class."""

    def __init__(self):
        """Customize the class init."""
        self.date = None
        self.name = None
        self.time = None
        self.note = None

    def add_date(self):
        """Set the task date."""
        utilities.show_add_task_title()
        while True:
            # Get the date of the task from the user
            task_date = input("\nWhat is the date of the task? \n"
                              "Please use 'DD/MM/YYYY format: ")
            try:
                task_date = datetime.datetime.strptime(task_date, fmt)
            except ValueError:
                utilities.show_add_task_title()
                print("Sorry '{}' is not in the correct date format. "
                      "Please try again.\n".format(task_date))
                continue
            else:
                self.date = task_date  # Set the date
                self.get_task_name()
                break

    def get_task_name(self):
        """Set the task name."""
        utilities.show_add_task_title()
        while True:
            task_name = str(input('\nWhat is the name of the task? '))
            if task_name == '':
                print("sorry, task name cannot be blank.")
                continue
            else:
                self.name = task_name
                print('Date = {}'.format(self.date))
                print('Name = {}'.format(self.name))
                break

