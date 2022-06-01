#!/usr/bin/python3
'''
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
'''

import requests

'''Data'''
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/70.0.3538.77 Safari/537.36"}


def top_ten(subreddit):
    url = "https://www.reddit.com/r/" + str(subreddit) + "/hot.json"
    res = requests.get(url, headers=header)
    i = 0
    if res.status_code == 200:
        titles = res.json().get("data").get("children")
        for t in titles:
            if i >= 10:
                break
            print(t.get("data").get("title"))
            i = i + 1
    else:
        print(None)
    return
