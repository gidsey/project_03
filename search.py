"""Search."""
import datetime
import shutil
import csv
import re
# import os

import utilities

fmt = '%d/%m/%Y'


def friendly_date(datein):
    """Return a freindly date."""
    return datetime.datetime.strftime(datein, fmt)


class Search(list):
    """Define the Search class."""

    def __init__(self):
        """Customize the class init."""
        self.results = []
        self.count = 0
        self.id = None
        self.date = None
        # Read the CSV file and store conetnt in a list
        with open('tasks.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            self.dataset = list(reader)
        self.numtasks = len(self.dataset)

    def date_search(self, exact_date):
        """Search for an exact date match."""
        for row in self.dataset[0:self.numtasks]:
            if row['task_date'] == str(exact_date):
                self.results.append(row)
        if self.results:
            self.show_results()
        else:
            from work_log import search_menu
            utilities.show_results_title()
            input('\nSorry, there are no tasks listed for {}\n\n'
                  'Press ENTER to return to the search menu.'.format(
                   friendly_date(exact_date)))
            search_menu()

    def range_search(self, start_date, end_date):
        """Serach accross a date range."""
        for row in self.dataset[0:self.numtasks]:
            task_date = datetime.datetime.strptime(
             row['task_date'], '%Y-%m-%d %H:%M:%S')
            if start_date <= task_date <= end_date:
                self.results.append(row)
        if self.results:
            self.show_results()
        else:
            from work_log import search_menu
            utilities.show_results_title()
            input('\nSorry, there are no tasks listed '
                  'within that date range.\n\n'
                  'Press ENTER to return to the search menu.')
            search_menu()

    def time_search(self, duration):
        """Serach for an exact duration match."""
        for row in self.dataset[0:self.numtasks]:
            if row['task_time'] == str(duration):
                self.results.append(row)
        if self.results:
            self.show_results()
        else:
            from work_log import search_menu
            utilities.show_results_title()
            input('\nSorry, there are no tasks listed for with a duration '
                  'of {} minutes.\n\nPress ENTER to return to the '
                  'search menu.'.format(duration))
            search_menu()

    def text_search(self, text):
        """Serach for an exact text match."""
        for row in self.dataset[0:self.numtasks]:
            if text.lower() in row['task_name'].lower() or \
                    text.lower() in row['task_notes'].lower():
                self.results.append(row)
        if self.results:
            self.show_results()
        else:
            from work_log import search_menu
            utilities.show_results_title()
            input("\nSorry, there are no tasks listed that include "
                  "'{}'.\n\nPress ENTER to return to the "
                  "search menu.".format(text))
            search_menu()

    def pattern_search(self, pattern):
        """Serach for an exact text match."""
        for row in self.dataset[0:self.numtasks]:
            if re.search(pattern, row['task_name']) or \
                 re.search(pattern, row['task_notes']):
                self.results.append(row)
        if self.results:
            self.show_results()
        else:
            from work_log import search_menu
            utilities.show_results_title()
            input("\nSorry, there are no tasks listed that match the pattern"
                  "'{}'.\n\nPress ENTER to return to the "
                  "search menu.".format(pattern))
            search_menu()

    def show_results(self):
        """Show the search results."""
        utilities.show_results_title()
        self.date = datetime.datetime.strptime(
             self.results[self.count]['task_date'],
             '%Y-%m-%d %H:%M:%S')
        f_date = friendly_date(self.date )
        print('\nResult {} of {}:\n'.format(self.count+1, len(self.results)))
        print('Date: {}'.format(f_date))
        print('Task: {}'.format(self.results[self.count]['task_name']))
        print('Time Spent (minutes): {}'.
              format(self.results[self.count]['task_time']))
        print('Notes: {}'.format(self.results[self.count]['task_notes']))
        self.id = self.results[self.count]['task_id']
        self.show_results_menu()

    def show_results_menu(self):
        """Show the results options."""
        from work_log import search_menu

        while True:

            selction = input('\n[N]ext, [E]dit, [D]elete, '
                             '[R]eturn to seach menu > ')

            if selction.upper() == 'N':  # Show next search result
                try:
                    self.count += 1
                    self.show_results()
                    break
                except IndexError:
                    utilities.show_results_title()
                    input('\nNo more results to show.\n\n'
                          'Press ENTER to return to the search menu.')
                    search_menu()
                    break

            if selction.upper() == 'E':  # Edit the entry
                self.edit_task()
                break

            if selction.upper() == 'D':  # Delete row from CSV file
                # Ref: https://tinyurl.com/y4je42ka
                confirm = input('\nDelete entry? (Y/N)')
                if confirm.upper() == 'Y':
                    fieldnames = [
                      'task_id',
                      'task_date',
                      'task_name',
                      'task_time',
                      'task_notes'
                    ]
                    with open('tasks.csv') as csvfile, \
                            open('temp.csv', 'w', newline='') as outputfile:
                        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                        writer = csv.DictWriter(outputfile,
                                                fieldnames=fieldnames)
                        for row in reader:
                            if not row['task_id'] == \
                                 self.results[self.count]['task_id']:
                                writer.writerow(
                                    {'task_id': row['task_id'],
                                     'task_date': row['task_date'],
                                     'task_name': row['task_name'],
                                     'task_time': row['task_time'],
                                     'task_notes': row['task_notes']
                                     })
                    shutil.move('temp.csv', 'tasks.csv')
                    utilities.show_serach_title()
                    input('Entry deleted successfully.\n\n'
                          'Press ENTER to return to the serach menu.')
                    search_menu()
                    break
                else:
                    search_menu()
                    break

            if selction.upper() == 'R':
                # Return to serach menu
                search_menu()
                break
            else:
                self.show_results()
                break

    def edit_task(self):
        """Edit the task."""
        utilities.show_edit_menu_options()
        edit_item = input("\nEnter 'a', 'b', 'c' 'd' or 'r': ")
        while True:
            if edit_item.upper() == 'A':  # Edit date
                utilities.show_edit_menu_options()
                print(self.id)
                print('\nCurrent date is {}'.format(self.date))
                new_date = input("\nPlease enter new date in 'DD/MM/YYYY format:")
                print(new_date)
                break
            if edit_item.upper() == 'B':  # Edit task
                utilities.show_edit_menu_options()
                break
            if edit_item.upper() == 'C':  # Edit time spent
                utilities.show_edit_menu_options()
                break
            if edit_item.upper() == 'D':  # Edit notes
                utilities.show_edit_menu_options()
                break
            if edit_item.upper() == 'R':
                from work_log import search_menu
                search_menu()
                break
            else:
                utilities.show_edit_menu_options()
                print("\nSorry, we did not recoginse '{}'"
                      ", please try again.".format(edit_item))
                continue


