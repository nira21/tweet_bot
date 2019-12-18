#coding; utf-8

from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime

def puttweet():

    twitter = OAuth1Session(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

    tweets = ["文章1",\
    "文章2",\
    "文章3",\
    "文章4",\
    "文章5"]
    randomtweet = tweets[random.randrange(len(tweets))]
    params = {"status": randomtweet}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
