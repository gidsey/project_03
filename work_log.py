"""Work log main file."""

import utilities

from tasks import Task


def main_menu():
    """Define the main menu."""
    utilities.show_main_menu_options()
    while True:
        selction = input("\nEnter 'a', 'b' or 'c' > ")

        if selction.upper() == 'A':
            add_new_task()
            break
        if selction.upper() == 'B':
            print('b')
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


if __name__ == "__main__":
    """Run the program."""
    main_menu()
