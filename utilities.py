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
    print('b) Search the existing entries')
    print('c) Quit')


def show_add_task_title():
    """Print the add task title."""
    clear_screen()
    print('\nWork Log : Add a task'.upper()+'\n'+'-'*22)


def show_results_title():
    """Print the results title."""
    clear_screen()
    print('\nWork Log : Search Results'.upper()+'\n'+'-'*26)


def show_serach_title():
    """Print the search title."""
    clear_screen()
    print('\nWork Log : Search'.upper()+'\n'+'-'*18)


def show_search_menu_options():
    """Print the main menu options."""
    clear_screen()
    print('\nWork Log : Search'.upper()+'\n'+'-'*18)
    print('What do you want to search by:\n')
    print('a) Exact date')
    print('b) Range of dates')
    print('c) Time spent')
    print('d) Text search')
    print('e) RegEx pattern\nor')
    print('[R]eturn to main menu')


def show_edit_title():
    """Print the edit title."""
    clear_screen()
    print('\nWork Log : Edit Entry'.upper()+'\n'+'-'*22)


def show_edit_menu_options():
    """Print the edit menu options."""
    print('Select the item you wish to edit:\n')
    print('a) Date')
    print('b) Task')
    print('c) Time spent')
    print('c) Notes')
    print('or')
    print('[R]eturn to search menu')
