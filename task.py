from pathlib import Path
from rich import print


class Task:
    """Creates a class for the tasks manipulation on the TO DO list"""

    def __init__(self, cache_path: Path):
        # TODO: read about protected member variables, and rename the members with _ prefix
        # Read: https://realpython.com/python-classes/#public-vs-non-public-members
        self.cache_path = cache_path
        # TODO: make read-only property for tasks
        # Read: https://realpython.com/python-property/#using-property-as-a-decorator
        self.tasks = []

        self.load_tasks()

    def load_tasks(self):
        if not self.cache_path.is_file():
            return

        with open(self.cache_path, mode="r", encoding="utf8") as cache_file:
            for line in cache_file:
                self.add_task(line.strip())

    def add_task(self, title: str):
        self.tasks.append(title)

    def print_tasks(self):
        for task in self.tasks:
            print(f'[bold green]{task}[/bold green]')

    def save_tasks(self):
        with open(self.cache_path, mode="w", encoding="utf8") as filename:
            for task in self.tasks:
                filename.write(task + '\n')

    def delete_tasks(self, index: int):
        index = index - 1
        self.tasks.pop(index)
