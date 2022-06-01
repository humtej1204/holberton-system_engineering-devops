#!/usr/bin/python3
'''
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
'''

import requests


def recurse(subreddit, hot_list=[], after=""):
    """List containing the titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'AngentMEGO'},
                       params={'after': after})

    if after is None:
        return hot_list

    if res.status_code == 200:
        res = res.json()
        after = res.get('data').get('after')
        hots = res.get('data').get('children')
        hot_list += list(map(lambda elm: elm.get('data').get('title'), hots))
        return recurse(subreddit, hot_list, after)
    return None
