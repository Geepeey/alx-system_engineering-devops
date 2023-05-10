#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """Recursive function to query the Reddit API"""
    if count_dict is None:
        count_dict = {}

    url = (
        "https://www.reddit.com/r/{}/hot.json"
        "?limit=100&after={}"
    ).format(subreddit, after)

    headers = {"User-Agent": "My Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            for word in word_list:
                if word.lower() in title:
                    count_dict[word] = count_dict.get(word, 0) + 1

        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, after, count_dict)

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")

    return count_dict.get(word_list[0], 0) if word_list else 0
