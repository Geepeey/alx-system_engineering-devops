#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 todo_list.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    try:
        response = requests.get(url)
        response.raise_for_status()
        employee_name = response.json().get('username')
    except requests.exceptions.HTTPError:
        print("Invalid employee ID provided.")
        sys.exit(1)
    except requests.exceptions.RequestException:
        print("An error occurred while accessing the API.")
        sys.exit(1)

    todo_url = url + "/todos"

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()
    except requests.exceptions.HTTPError:
        print("An error occurred while accessing the employee's TODO list.")
        sys.exit(1)
    except requests.exceptions.RequestException:
        print("An error occurred while accessing the API.")
        sys.exit(1)

    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

    print("TODO list data exported to file: {}".format(filename))
