#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[]):
    """Return list of all hot post"""
    url = "https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "My Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
