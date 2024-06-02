#!/usr/bin/python3
"""A Python script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress and exports
the data to a CSV file.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_list_csv.py <employee_id>")
        exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    done_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_tasks_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done_tasks_count, total_tasks))

    for task in done_tasks:
        print(f"\t {task['title']}")

    # Export todo list to CSV
    file_name = f"{employee_id}.csv"
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            task_status = "True" if task["completed"] else "False"
            csv_writer.writerow([
                employee_id,
                user.get("name"),
                task_status,
                task["title"]
            ])

    print(f"Employee {user.get('name')}'s todo list exported to {file_name}")