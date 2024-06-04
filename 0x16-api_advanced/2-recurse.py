import requests

def recurse(subreddit, hot_list=[]):
  """Fetches titles of all hot articles for a subreddit recursively.

  Args:
      subreddit: The name of the subreddit (without 'r/').
      hot_list (list, optional): An empty list to accumulate titles. Defaults to [].

  Returns:
      A list containing titles of all hot articles or None if the subreddit is invalid.
  """

  # Base URL for subreddit hot listings
  url = f"https://reddit.com/r/{subreddit}/hot.json?limit=100&after={hot_list[-1]['name'] if hot_list else ''}"

  try:
    # Send GET request with custom User-Agent to avoid throttling
    response = requests.get(url, headers={"User-Agent": "MyCoolScript"}, allow_redirects=False)
    response.raise_for_status()  # Raise exception for non-2xx status codes

    # Parse JSON response
    data = response.json()

    # Check for valid subreddit data (presence of 'data' key)
    if 'data' in data and 'children' in data['data']:
      # Extract titles and update hot_list
      hot_list.extend(post['data']['title'] for post in data['data']['children'])

      # Check for 'after' key indicating next page (recursion base case)
      if 'after' in data['data']:
        return recurse(subreddit, hot_list)
      else:
        return hot_list  # No more pages, return accumulated titles
    else:
      return None  # No valid data found

  except requests.exceptions.RequestException:
    # Handle request errors gracefully
    return None

  except Exception as e:
    # Handle any unexpected errors
    print(f"An error occurred: {e}")
    return None
