#!/usr/bin/python3
'''
function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
'''

import requests

'''Data'''
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/70.0.3538.77 Safari/537.36"}


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/" + str(subreddit) + "/about.json"
    res = requests.get(url, headers=header)
    if res.status_code == 200:
        subs = res.json().get("data").get("subscribers")
        return subs
    return 0
