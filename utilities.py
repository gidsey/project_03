"""Utilities."""
import os


def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == 'nt' else "clear")


def show_main_menu_options():
    """Print the main menu options."""
    clear_screen()
    print('\nWork Log : Main Menu'.upper()+'\n'+'-'*20)
    print('What would you like to do?\n')
    print('a) Add a new entry')
    print('b) Serach the existing entries')
    print('c) Quit')


def show_add_task_title():
    """Print the main menu options."""
    clear_screen()
    print('\nWork Log : Add a task'.upper()+'\n'+'-'*22)


def show_search_menu_options():
    """Print the main menu options."""
    clear_screen()
    print('\nWork Log : Search Menu'.upper()+'\n'+'-'*20)
    print('What do you want to search by:\n')
    print('a) Exact date')
    print('b) Range of dates')
    print('c) Time spent')
    print('d) Exact search')
    print('e) RegEx pattern')
    print('f) [Return to main menu]')

