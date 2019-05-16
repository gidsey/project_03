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
                self.add_name()
                break

    def add_name(self):
        """Set the task name."""
        utilities.show_add_task_title()
        while True:
            task_name = str(input('\nWhat is the name of the task? '))
            if task_name == '':
                print("sorry, task name cannot be blank.\n")
                continue
            else:
                self.name = task_name
                self.add_time()
                break

    def add_time(self):
        """Set the task time spent in minutes."""
        utilities.show_add_task_title()
        while True:
            try:
                task_time = int(input("\nTime spend on task "
                                      "(rounded minutes): "))
            except ValueError:
                utilities.show_add_task_title()
                print("Error. Please enter the number of minutes "
                      "as a whole number.\n")
                continue
            else:
                self.time = task_time
                self.add_notes()
                break

    def add_notes(self):
        """Add notes to the task (optional)."""
        utilities.show_add_task_title()
        while True:
            task_notes = str(input('\nAdd a note to this task? (optional): '))
            if task_notes == '':
                self.notes = None
                self.print_output()
                break
            else:
                self.notes = task_notes
                self.print_output()
                break

    def print_output(self):
        """debugging."""
        print('\nDate = {}'.format(self.date))
        print('Name = {}'.format(self.name))
        print('Time = {}'.format(self.time))
        print('Notes = {}'.format(self.notes))
        print()


