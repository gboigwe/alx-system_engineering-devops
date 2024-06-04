#!/usr/bin/python3


"""API subreddit checking"""


import requests


def recurse(subreddit, hot_list=[]):
    """Fetches titles of all hot articles for a subreddit recursively.
    Returns:
        List containing titles of all hot articles or None if invlid subreddit.
    """

    url = "https://reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit,
        hot_list[-1]['name'] if hot_list else '')
    try:
        response = requests.get(
                url,
                headers={"User-Agent": "MyCoolScript"},
                allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            hot_list.extend(
                post['data']['title'] for post in data['data']['children'])
            if 'after' in data['data']:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
