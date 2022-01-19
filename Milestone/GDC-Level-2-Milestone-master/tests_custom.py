import pytest
from solve_me import TasksCommand


def test_manual():
    tasks = TasksCommand()

    data = open("tasks.txt", "r+")
    data.truncate(0)

    # Existing cases
    tasks.run("add", [3, "Task 1"])
    tasks.run("add", [4, "Task 2"])
    tasks.run("add", [6, "Task 3"])

    # Adding new case
    tasks.run("add", [3, "Task 4"])

    lines = data.readlines()

    print(lines)
    print(lines == ["3 Task 4\n", "4 Task 1\n", "5 Task 2\n", "6 Task 3\n"])


def test_shailesh():
    tasks = TasksCommand()

    data = open("tasks.txt", "r+")
    data.truncate(0)

    # Existing cases
    tasks.run("add", [6, "Task 3"])
    tasks.run("add", [4, "Task 2"])
    tasks.run("add", [3, "Task 1"])

    # Adding new case
    tasks.run("add", [3, "Task 4"])

    lines = data.readlines()

    print(lines)
    print(lines == ["3 Task 4\n", "4 Task 1\n", "5 Task 2\n", "6 Task 3\n"])
