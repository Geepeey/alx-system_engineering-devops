#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to CSV format.

Usage: python3 export_todo_csv.py USER_ID

USER_ID: The ID of the user whose to-do list will be exported.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(user_url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    user_todos = requests.get(user_url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in user_todos:
            writer.writerow([user_id, user_name, todo.get("completed"), todo.get("title")])
