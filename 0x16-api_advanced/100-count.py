#!/usr/bin/python3
"""
    counts the number of words in all hot posts of a given subreddit
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
        counts of given words found in hot posts of a subreddit.
        subreddit (str): The subreddit to search
        word_list (list): The list of words to search for in post titles
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    vals = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(
                  url,
                  headers=headers,
                  params=vals,
                  allow_redirects=False)
    try:
        results = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                key = word.lower()
                if instances.get(key) is None:
                    instances[key] = times
                else:
                    instances[key] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
        return

    count_words(subreddit, word_list, instances, after, count)
