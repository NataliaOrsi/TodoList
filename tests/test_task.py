import textwrap

from task import Task


def test_tasks_no_cache(tmp_path, capsys):
    cache_path = tmp_path / "tasks.txt"
    assert not cache_path.is_file()

    task = Task(cache_path=cache_path)
    assert task.tasks == []

    task.add_task("foo")
    assert task.tasks == ["foo"]

    task.add_task("bar")
    assert task.tasks == ["foo", "bar"]

    task.print_tasks()
    output = textwrap.dedent("""\
    foo
    bar
    """)
    assert capsys.readouterr().out == output

    task.save_tasks()
    assert cache_path.is_file()
    assert cache_path.read_text(encoding="utf8") == output

    task.delete_tasks(2)
    assert task.tasks == ["foo"]

    task.delete_tasks(1)
    assert task.tasks == []

    task.load_tasks()
    assert task.tasks == ["foo", "bar"]


def test_tasks_with_cache(tmp_path, capsys):
    # TODO: create test that start with existing populated cache
    pass
