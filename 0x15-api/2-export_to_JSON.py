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
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)

# if __name__ == "__main__":
#     employee_id = sys.argv[1]
#     url = "https://jsonplaceholder.typicode.com/"

#     # Get employee name
#     response = requests.get(url + "users/{}".format(employee_id))
#     if response.status_code == 200:
#         user = response.json()
#     else:
#         print("Failed to get employee name for ID {}".format(employee_id))
#         # exit(1)

#     # Get employee's todo list
#     todos_response = requests.get(
#         url + "todos", params={"userId": employee_id})
#     if todos_response.status_code == 200:
#         todos = todos_response.json()
#     else:
#         print("Failed to get todo list for employee {}"
#               .format(user.get('name')))
#         # exit(1)

#     # Export todo list to JSON
#     file_name = "{}.json".format(employee_id)
#     todo_list = {
#         employee_id: [
#             {
#                 "task": todo["title"],
#                 "completed": todo["completed"],
#                 "username": user.get("name")
#             }
#             for todo in todos
#         ]
#     }

#     with open(file_name, 'w') as jsonfile:
#         json.dump(todo_list, jsonfile)

#     print("Employee {}'s todo list exported to {}"
#           .format(user.get('name'), file_name))
