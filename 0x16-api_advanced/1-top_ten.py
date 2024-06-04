#!/usr/bin/python3


"""API subreddit checking"""


import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts from a subreddit.
    Args:
        subreddit: The name of the subreddit (without 'r/').
        Prints the titles or None if invalid subreddit.
    """

    url = "https://reddit.com/r/{}/hot.json?limit=10&raw_json=1".format(
        subreddit)

    try:
        response = requests.get(url, headers={"User-Agent": "python-requests/2.28.1"},
                                allow_redirects=False)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
            else:
                print(None)

    except requests.exceptions.RequestException:
        print(None)
    except Exception as e:
        print(f"An error occurred: {e}")

        print(None)
