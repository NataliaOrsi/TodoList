import enum
from pathlib import Path
from rich import print

from task import Task

@enum.unique
class MenuAction(enum.Enum):
    ACTION_ADD_TASK = 1
    ACTION_VIEW_LIST = 2
    ACTION_DELETE_TASK = 3
    ACTION_EXIT = 4

def welcome_message():
    print("\n[bold magenta]Welcome to the tasks planner[/bold magenta]")
    print('[bold magenta]---------------------------[/bold magenta]\n')


def menu():
    print('Menu: \n')
    print(f'{MenuAction.ACTION_ADD_TASK.value}. [bold blue]Add a task[/bold blue]')
    print(f'{MenuAction.ACTION_VIEW_LIST.value}. [bold blue]View your tasks list[/bold blue]')
    print(f'{MenuAction.ACTION_DELETE_TASK.value}. [bold blue]Delete a task[/bold blue]')
    print(f'{MenuAction.ACTION_EXIT.value}. [bold blue]Exit the application[/bold blue]')


if __name__ == '__main__':
    task_path = Path("tasks.txt")
    tasks = Task(cache_path=task_path)

    welcome_message()
    while True:
        menu()
        answer = int(input("\nYour answer: "))
        print('----------------\n')

        try:
            answer = MenuAction(answer)
        except ValueError:
            print("Try again")
            continue

        match answer:
            case MenuAction.ACTION_ADD_TASK:
                to_do = input('Write your tasks: ')
                tasks.add_task(to_do)
            case MenuAction.ACTION_VIEW_LIST:
                print('Your tasks: ')
                print('-------------\n')
                tasks.print_tasks()
                print('\n')
                access_menu = input('Back to menu?(y/n) ')
                print('\n')
                if access_menu == 'y':
                    continue
                else:
                    print("[bold red]Exiting...[/bold red]")
                    break
            case MenuAction.ACTION_DELETE_TASK:
                to_delete = int(input('Which task(s) to delete?[1, 2, 3..] '))

                tasks.delete_tasks(to_delete)
            case MenuAction.ACTION_EXIT:
                print("[bold red]Exiting...[/bold red]\n")

                tasks.save_tasks()
                print('Your tasks: ')
                print('-------------\n')
                tasks.print_tasks()
                break
