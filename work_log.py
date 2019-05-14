"""Work log main file."""
import datetime

from utilities import clear_screen
# from tasks import Add_New

fmt = '%d/%m/%Y'

def main_menu():
    """Define the main menu."""
    show_main_menu_options()
    while True:
        selction = input("\nEnter 'a', 'b' or 'c' > ")

        if selction.upper() == 'A':
            add_new_task()
            break
        if selction.upper() == 'B':
            print('b')
        if selction.upper() == 'C':
            clear_screen()
            print('\nThanks for using WORK LOG!\n')
            break
        else:
            show_main_menu_options()
            print("\nSorry, we did not recoginse '{}'"
                  ", plasee try again.".format(selction))


def show_main_menu_options():
    """Print the main menu options."""
    clear_screen()
    print('\nWork Log : Main Menu'.upper()+'\n'+'-'*20)
    print('What would you like to do?')
    print('a) Add a new entry')
    print('b) Serach the existing entries')
    print('c) Quit')


def show_add_task_title():
    """Print the main menu options."""
    clear_screen()
    print('\nWork Log : Add a task'.upper()+'\n'+'-'*24)


def add_new_task():
    """Add a new task."""
    task = []
    show_add_task_title()
    while True:
        # Get the date of the task
        task_date = input("Date of the task? \n"
                          "Please use 'DD/MM/YYYY format: ")
        try:
            task_date = datetime.datetime.strptime(task_date, fmt)
        except ValueError:
            print('*** ERROR ***')
            continue
        else:
            task.append(task_date)

            show_add_task_title()
            task_name = str(input('What is the task? '))
            task.append(task_name)
            print(task)


if __name__ == "__main__":
    """Run the program."""
    main_menu()
