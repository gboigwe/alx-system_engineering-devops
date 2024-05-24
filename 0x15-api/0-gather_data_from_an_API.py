#!/usr/bin/python3
"""A Python script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    done_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_tasks_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done_tasks_count, total_tasks))

    for task in done_tasks:
        print(f"\t {task['title']}")
