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
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

# if __name__ == "__main__":
#     employee_id = sys.argv[1]
#     url = "https://jsonplaceholder.typicode.com/"
#     response = requests.get(url + "users/{}".format(employee_id))
#     if response.status_code == 200:
#         user = response.json()
#     else:
#         print("Failed to get employee name for ID {}".format(employee_id))
#         exit(1)

#     # Get employee's todo list
#     todos_response = requests.get(url + "todos", params={
#         "userId": employee_id
#         })
#     if todos_response.status_code == 200:
#         todos = todos_response.json()
#     else:
#         print("Failed to get todo list for employee {}"
#               .format(user.get('name')))
#         exit(1)

#     # Export todo list to CSV
#     file_name = "{}.csv".format(employee_id)
#     with open(file_name, 'w', newline='') as csvfile:
#         csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#         for task in todos:
#             task_status = "True" if task["completed"] else "False"
#             csv_writer.writerow([
#                 employee_id,
#                 user.get("name"),
#                 task_status,
#                 task["title"]
#             ])

#     print("Employee {}'s todo list exported to {}"
#           .format(user.get('name'), file_name))
