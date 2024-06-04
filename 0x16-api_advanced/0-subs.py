#!/usr/bin/python3
"""
A function that queries the Reddit API
"""


import requests


def number_of_subscribers(subreddit):
    """API subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom User-Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return (0)
    except requests.RequestException as err:
        return (0)
