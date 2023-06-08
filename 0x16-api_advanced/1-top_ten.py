#!/usr/bin/python3
"""
    Function to print the top ten posts
    on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
