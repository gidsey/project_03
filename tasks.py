"""Tasks."""
import datetime
import csv
import os

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
                self.add_entry()
                break
            else:
                self.notes = task_notes
                self.add_entry()
                break

    def add_entry(self):
        """Add the enytr to task.csv."""
        fieldnames = [
            'task_date',
            'task_name',
            'task_time',
            'task_notes'
        ]

        file_exists = os.path.isfile('tasks.csv')
        # check whether file exists
        # ref: https://tinyurl.com/y67yexqj

        with open('tasks.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                    'task_date': self.date,
                    'task_name': self.name,
                    'task_time': self.time,
                    'task_notes': self.notes
                    })
        self.print_output()
        input("The entry has been added. "
              "Press ENTER to return to the main menu.")
        print('yes!')

    def print_output(self):
        """debugging."""
        print('\nDate = {}'.format(self.date))
        print('Name = {}'.format(self.name))
        print('Time = {}'.format(self.time))
        print('Notes = {}'.format(self.notes))
        print()

