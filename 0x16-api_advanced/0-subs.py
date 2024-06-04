#!/usr/bin/python3
"""API subreddit checking"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python-requests/2.28.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except (requests.exceptions.RequestException, KeyError):
        return 0
