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
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee name
    response = requests.get(url + "users/{}".format(employee_id))
    if response.status_code == 200:
        user = response.json()
    else:
        print(f"Failed to get employee name for ID {employee_id}")
        exit(1)

    # Get employee's todo list
    todos_response = requests.get(url + "todos", params={
        "userId": employee_id
        })
    if todos_response.status_code == 200:
        todos = todos_response.json()
    else:
        print(f"Failed to get todo list for employee {user.get('name')}")
        exit(1)

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
