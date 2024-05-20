#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./todo.py EMPLOYEE_ID")
        exit(1)

    employee_id = int(sys.argv[1])
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    response = requests.get(url)
    todos = response.json()

    done_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_tasks_count = len(done_tasks)

    employee_name = done_tasks[0]["userId"] if done_tasks else "Unknown"

    print(f"""
            Employee {employee_name}
            is done with tasks({done_tasks_count}/{total_tasks}):
            """)

    for task in done_tasks:
        print(f"\t {task['title']}")
