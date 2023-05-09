#!/usr/bin/python3
"""A function that queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit Api"""
    
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
