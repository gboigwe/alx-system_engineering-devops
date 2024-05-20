#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)

    response = requests.get(url)
    todos = response.json()

    done_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_tasks_count = len(done_tasks)

    employee_name = done_tasks[0]["userId"] if done_tasks else "Unknown"

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_tasks_count, total_tasks))

    for task in done_tasks:
        print(f"\t {task['title']}")
