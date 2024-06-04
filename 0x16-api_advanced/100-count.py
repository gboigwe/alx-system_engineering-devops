#!/usr/bin/python3


"""API subreddit checking"""


import requests
from collections import Counter


def count_words(subreddit, word_list, word_counts=Counter()):
    """Fetches case-insensitive keyword counts
        from hot article titles recursively.
    Prints the sorted keyword counts in descending order.
    """
    url = "https://reddit.com/r/{}/hot.json?limit=100&after={}".format(
            subreddit,
            word_counts.get('after', ''))
    try:
        response = requests.get(url,
                                headers={"User-Agent": "MyCoolScript"},
                                allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            lowercase_words = []
            for post in data['data']['children']:
                for word in post['data']['title'].lower().split():
                    lowercase_words.append(word.strip(".,!?"))
            titles = lowercase_words

            word_counts.update(word for word in titles if word in word_list)
            if 'after' in data['data']:
                count_words(subreddit, word_list, word_counts)
            else:
                for word, count in word_counts.most_common():
                    if count > 0:  # Skip words with no matches
                        print(f"{word.lower()}: {count}")
                    else:
                        pass
    except requests.exceptions.RequestException:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
