#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
from urllib import request, error


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        with request.urlopen(url) as response:
            users = json.loads(response.read().decode())

        dictionary = {}
        for user in users:
            user_id = user.get('id')
            username = user.get('username')
            user_todos = requests.get(
                user_url + "todos", params={"userId": user_id}).json()
            url = url + '/todos/'
            with request.urlopen(url) as response:
                tasks = json.loads(response.read().decode())

            dictionary[user_id] = []
            for task in tasks:
                dictionary[user_id].append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                })

        with open('todo_all_employees.json', 'w') as file:
            json.dump(dictionary, file)

    except error.HTTPError as e:
        print('HTTPError: {}'.format(e.code), file=sys.stderr)
    except error.URLError as e:
        print('URLError: {}'.format(e.reason), file=sys.stderr)
    except Exception as e:
        print('Error: {}'.format(e), file=sys.stderr)
