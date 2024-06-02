#!/usr/bin/python3
"""A Python script that, using this REST API,
exports the todo lists of all employees to a
JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Get all users
    users_response = requests.get(url + "users")
    if users_response.status_code == 200:
        users = users_response.json()
    else:
        print("Failed to get users")
        exit(1)

    # Get all todos
    todos_response = requests.get(url + "todos")
    if todos_response.status_code == 200:
        todos = todos_response.json()
    else:
        print("Failed to get todos")
        exit(1)

    # Group todos by user
    todo_lists = {}
    for todo in todos:
        user_id = todo["userId"]
        username = next(
            (user["name"] for user in users if user["id"] == user_id), "Unknown"
        )
        task_data = {
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"],
        }
        if user_id in todo_lists:
            todo_lists[user_id].append(task_data)
        else:
            todo_lists[user_id] = [task_data]

    # Export todo lists to JSON
    file_name = "todo_all_employees.json"
    with open(file_name, "w") as jsonfile:
        json.dump(todo_lists, jsonfile)

    print(f"Todo lists of all employees exported to {file_name}")
