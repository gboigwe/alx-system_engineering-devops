#!/usr/bin/python3
"""A Python script that, using this REST API,
for a given employee ID, returns information
about his/her todo list progress and exports
the data to a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
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
    todos_response = requests.get(
        url + "todos", params={"userId": employee_id})
    if todos_response.status_code == 200:
        todos = todos_response.json()
    else:
        print(f"Failed to get todo list for employee {user.get('name')}")
        exit(1)

    # Export todo list to JSON
    file_name = f"{employee_id}.json"
    todo_list = {
        employee_id: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user.get("name")
            }
            for todo in todos
        ]
    }

    with open(file_name, 'w') as jsonfile:
        json.dump(todo_list, jsonfile)

    print(f"Employee {user.get('name')}'s todo list exported to {file_name}")
