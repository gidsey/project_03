"""Search."""
import datetime
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

    def __init__(self, ):
        """Customize the class init."""
        self.results = []
        self.count = 0
        # Read the CSV file and store conetnt in a list
        with open('tasks.csv', newline='') as csvfile: 
            taskreader = csv.DictReader(csvfile, delimiter=',')
            self.dataset = list(taskreader)
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
            input('\nSorry, there are no tasks listed within that date range.\n\n'
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
        # pattern = "r'" + pattern + "'"
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
        f_date = datetime.datetime.strptime(
             self.results[self.count]['task_date'],
             '%Y-%m-%d %H:%M:%S')
        f_date = friendly_date(f_date)
        print('\nResult {} of {}:\n'.format(self.count+1, len(self.results)))
        print('Date: {}'.format(f_date))
        print('Task: {}'.format(self.results[self.count]['task_name']))
        print('Time Spent (minutes): {}'.
              format(self.results[self.count]['task_time']))
        print('Notes: {}'.format(self.results[self.count]['task_notes']))
        self.show_results_menu()

    def show_results_menu(self):
        """Show the results options."""
        from work_log import search_menu

        while True:

            selction = input('\n[N]ext, [E]dit, [D]elete, '
                             '[R]eturn to seach menu > ')

            if selction.upper() == 'N':
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

            if selction.upper() == 'E':
                pass

            if selction.upper() == 'D':
                print(self.results[self.count])
                break

            if selction.upper() == 'R':
                search_menu()
                break
            else:
                self.show_results()
                break
