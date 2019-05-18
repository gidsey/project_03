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
            print('\nThanks for using WORK LOG!\n')
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
        else:
            utilities.show_search_menu_options()
            print("\nSorry, we did not recoginse '{}'"
                  ", please try again.".format(selction))


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
            s = Search()
            s.date_search(search_input)
            break


if __name__ == "__main__":
    """Run the program."""
    main_menu()
