"""Work log main file."""

import datetime

import utilities
from tasks import Task
from search import Search


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
            search_menu()
            break
        if selction.upper() == 'C':
            utilities.clear_screen()
            print('\nThanks for using WORK LOG :)\n')
            break
        else:
            utilities.show_main_menu_options()
            print("\nSorry, we did not recoginse '{}'"
                  ", please try again.".format(selction))


def add_new_task():
    """Create a class instance and populate it."""
    t = Task()
    t.add_date()


def search_menu():
    """Show the serach menu."""
    utilities.show_search_menu_options()

    while True:
        selction = input("\nEnter 'a', 'b', 'c', 'd', 'e' or 'r' > ")

        if selction.upper() == 'A':  # Date search
            search_date()
            break
        if selction.upper() == 'B':  # Range search
            search_daterange()
            break
        if selction.upper() == 'C':  # Time search
            search_time()
            break
        if selction.upper() == 'D':  # Text search
            search_text()
            break
        if selction.upper() == 'E':  # RegEx search
            search_regex()
            break
        if selction.upper() == 'R':  # Return to menu
            main_menu()
            break
        else:
            utilities.show_search_menu_options()
            print("\nSorry, we did not recoginse '{}'"
                  ", please try again.".format(selction))


def search_date():
    """Search by exact date."""
    utilities.show_add_task_title()
    while True:
        search_input = input("\nEnter the date that you wish to search for.\n"
                             "Please use 'DD/MM/YYYY format: ")
        try:
            search_input = datetime.datetime.strptime(search_input, fmt)
        except ValueError:
            utilities.show_add_task_title()
            print("\nSorry '{}' is not in the correct date format. "
                  "Please try again.".format(search_input))
            continue
        else:
            s = Search()
            s.date_search(search_input)
            break


def search_daterange():
    """Search by date range."""
    utilities.show_add_task_title()
    while True:
        start_date = input("\nEnter the first date in the range "
                           "to search for.\nPlease use 'DD/MM/YYYY format: ")
        try:
            start_date = datetime.datetime.strptime(start_date, fmt)
        except ValueError:
            utilities.show_add_task_title()
            print("\nSorry '{}' is not in the correct date format. "
                  "Please try again.".format(start_date))
            continue

        else:
            utilities.show_add_task_title()
            end_date = input("\nEnter the second date in the range "
                             "to search for.\nPlease use 'DD/MM/YYYY format: ")
            try:
                end_date = datetime.datetime.strptime(end_date, fmt)
            except ValueError:
                utilities.show_add_task_title()
                print("\nSorry '{}' is not in the correct date format. "
                      "Please try again.".format(end_date))
            else:
                # print(start_date)
                # print(end_date)
                range = abs(end_date - start_date)  # convert to a positive
                print(range)
                # s = Search()
                # s.date_search(search_input)
                break


def search_time():
    """Search duration in minutes."""
    utilities.show_add_task_title()
    while True:
        search_input = input("\nEnter the time spent in whole minutes: ")
        try:
            search_input = int(search_input)
        except ValueError:
            utilities.show_add_task_title()
            print("\nSorry '{}' is not in the correct format. "
                  "Please try again.\n".format(search_input))
            continue
        else:
            s = Search()
            s.time_search(search_input)
            break


def search_text():
    """Search the text in task name and notes."""
    utilities.show_add_task_title()
    while True:
        search_input = input("\nEnter the text to serach for: ")
        try:
            search_input = str(search_input)
        except ValueError:
            utilities.show_add_task_title()
            print("\nSorry '{}' is not in the correct format. "
                  "Please try again.\n".format(search_input))
            continue
        else:
            s = Search()
            s.text_search(search_input)
            break


def search_regex():
    """Search the text in task name using a RegEx pattern."""
    utilities.show_add_task_title()
    while True:
        search_input = input("\nEnter the RegEx pattern to use: ")
        try:
            search_input = str(search_input)
        except ValueError:
            utilities.show_add_task_title()
            print("\nSorry '{}' is not in the correct format. "
                  "Please try again.\n".format(search_input))
            continue
        else:
            s = Search()
            s.pattern_search(search_input)
            break


if __name__ == "__main__":
    """Run the program."""
    main_menu()
