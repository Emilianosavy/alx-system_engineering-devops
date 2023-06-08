#!/usr/bin/python3
"""
    queries a list of all top posts on a given Reddit subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
        Return: a list of titles of all top posts on a subreddit
    """
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(
                  link,
                  headers=headers,
                  params=parameters,
                  allow_redirects=False)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for kid in results.get("children"):
        hot_list.append(kid.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
