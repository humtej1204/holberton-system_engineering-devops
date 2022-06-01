#!/usr/bin/python3
'''
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
'''

import requests

'''Data'''
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/70.0.3538.77 Safari/537.36"}


def recurse(subreddit, hot_list=[], after=""):
    """List containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/" + str(subreddit) + "/hot.json"
    res = requests.get(url, headers=header,
                       params={'after': after})

    if after is None:
        return hot_list

    if res.status_code == 200:
        res = res.json()
        after = res.get('data').get('after')
        hots = res.get('data').get('children')
        #hot_list += list(map(lambda elm: elm.get('data').get('title'), hots))
        for l in hots:
            hot_list.append(l.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    return None
