#!/usr/bin/python3

"""
Accessing a REST API for todo lists of employees.

Export the data into JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    employee_name = response.json().get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    todo_list = []
    for task in tasks:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": employee_name}
        todo_list.append(task_dict)

    output = {employee_id: todo_list}

    with open(f"{employee_id}.json", mode='w') as file:
        json.dump(output, file, indent=4)
