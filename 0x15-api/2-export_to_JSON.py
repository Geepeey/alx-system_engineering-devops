#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/"
    user_dict = requests.get(user_url + "users/{}".format(user_id)).json()
    user_name = user_dict.get("username")
    user_todos = requests.get(
        user_url + "todos",
        params={"userId": user_id}).json()
    task_list = [{
        "task": t.get("title"),
        "completed": t.get("completed"),
        "username": user_name
    } for t in user_todos]

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: task_list}, jsonfile)
