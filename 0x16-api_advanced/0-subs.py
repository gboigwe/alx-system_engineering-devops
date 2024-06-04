#!/usr/bin/python3
"""
A function that queries the Reddit API
"""


import requests


def number_of_subscribers(subreddit):
    """API subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python-requests/2.28.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except requests.RequestException as err:
        return 0
