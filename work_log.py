"""Work log main file."""

import csv
import datetime

import utilities
from tasks import Task

fmt = '%d/%m/%Y'


def main_menu():
    """Define the main menu."""
    utilities.show_main_menu_options()
    while True:
        selction = input("\nEnter 'a', 'b' or 'c' > ")

        if selction.upper() == 'A':
            add_new_task()
            break
        if selction.upper() == 'B':
            go_search()
            break
        if selction.upper() == 'C':
            utilities.clear_screen()
            print('\nThanks for using WORK LOG!\n')
            break
        else:
            utilities.show_main_menu_options()
            print("\nSorry, we did not recoginse '{}'"
                  ", plasee try again.".format(selction))


def add_new_task():
    """Create a class instance and populate it."""
    t = Task()
    t.add_date()


def go_search():
    """Show the serach menu."""
    utilities.show_search_menu_options()

    while True:
        selction = input("\nEnter 'a', 'b', 'c', 'd', 'e' or 'f' > ")

        if selction.upper() == 'A':
            serach_date()
            break
        if selction.upper() == 'B':
            print('B')
            break
        if selction.upper() == 'C':
            print('C')
            break
        if selction.upper() == 'D':
            print('D')
            break
        if selction.upper() == 'E':
            print('E')
            break
        if selction.upper() == 'F':
            main_menu()
            break


def serach_date():
    """Serach by exact date."""
    utilities.show_add_task_title()
    while True:
        search_input = input("\nEnter the date that you wish to serach for.\n"
                             "Please use 'DD/MM/YYYY format: ")
        try:
            search_input = datetime.datetime.strptime(search_input, fmt)
        except ValueError:
            utilities.show_add_task_title()
            print("\nSorry '{}' is not in the correct date format. "
                  "Please try again.\n".format(search_input))
            continue
        else:
            search(search_input)
            break


def search(exact_date):
    """Return the serach results."""
    results = []
    exact_date_freindly = datetime.datetime.strftime(exact_date, fmt)
    with open('tasks.csv', newline='') as csvfile:
        taskreader = csv.DictReader(csvfile, delimiter=',')
        rows = list(taskreader)
        for row in rows[0:len(rows)]:
            if row['task_date'] == str(exact_date):
                results.append(row)
        if results:
            utilities.show_add_task_title()
            print('\nThere are {} tasks listed for {}:'
                  .format(len(results), exact_date_freindly))
        else:
            utilities.show_add_task_title()
            print('\nThere are no tasks listed for {}'.format(exact_date_freindly))


if __name__ == "__main__":
    """Run the program."""
    main_menu()
