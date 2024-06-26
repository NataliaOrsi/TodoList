from pathlib import Path
from rich import print


class Task:
    """Creates a class for the tasks manipulation on the TO DO list"""

    def __init__(self, cache_path: Path):
        self._cache_path = cache_path

        self._tasks = []

        self.load_tasks()

    @property
    def tasks(self) -> list[str]:
        return self._tasks[:]

    @property
    def cache_path(self):
        return self._cache_path

    def load_tasks(self):
        if not self._cache_path.is_file():
            return

        with open(self._cache_path, mode="r", encoding="utf8") as cache_file:
            for line in cache_file:
                self.add_task(line.strip())

    def add_task(self, title: str):
        self._tasks.append(title)

    def print_tasks(self):
        for task in self._tasks:
            print(f'[bold green]{task}[/bold green]')

    def save_tasks(self):
        with open(self._cache_path, mode="w", encoding="utf8") as filename:
            for task in self._tasks:
                filename.write(task + '\n')

    def delete_tasks(self, index: int):
        index = index - 1
        self._tasks.pop(index)
