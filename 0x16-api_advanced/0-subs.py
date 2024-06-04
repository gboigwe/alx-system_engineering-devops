#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    username = 'agegee123'
    password = '72Reddit'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/agegee123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return (0)

# #!/usr/bin/python3
# """API subreddit checking"""


# import json
# import requests
# import sys


# def number_of_subscribers(subreddit):
#     """
#     Returns the number of subscribers for a given subreddit.
#     If the subreddit is invalid, returns 0.
#     """

#     url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
#     headers = {"User-Agent": "python-requests/2.28.1"}

#     try:
#         response = requests.get(url, headers=headers, allow_redirects=False)
#         response.raise_for_status()
#         data = response.json()
#         subscribers = data["data"]["subscribers"]
#         return subscribers
#     except (requests.exceptions.RequestException, KeyError):
#         return 0
