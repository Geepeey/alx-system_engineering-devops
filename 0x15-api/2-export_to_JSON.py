#!/usr/bin/python3

"""
Accessing a REST API for todo lists of employees.

Export the data into JSON format.
"""

import json
import requests
import sys
import csv

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    employee_name = response.json().get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    # Write tasks to JSON
    data = {employee_id: []}
    for task in tasks:
        task_status = True if task.get('completed') else False
        task_title = task.get('title')
        data[employee_id].append({
            'task': task_title,
            'completed': task_status,
            'username': employee_name
        })

    with open(f"{employee_id}.json", mode='w') as file:
        json.dump(data, file)

    with open(f"{employee_id}.json", mode='r') as file:
        print(file.read().strip())
