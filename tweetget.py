
import tweepy
import pandas as pd
import datetime

import os
from dotenv import load_dotenv
from os.path import join, dirname
from requests_oauthlib import OAuth1Session
import oauth2 as oauth
# TweepyAPI KEY

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
#tweepyの設定
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
columns_name=["TW_NO","TW_TIME","TW_TEXT","RT","FAV"]
#ここで取得したいツイッターアカウントIDを指定する
tw_id="frags_ruiz"
#ツイート取得
def get_tweets():
    tweet_data = []
    for tweet in tweepy.Cursor(api.user_timeline,screen_name = tw_id,exclude_replies = True).items():
        tweet_data.append([tweet.id,tweet.created_at,tweet.created_at+datetime.timedelta(hours=9),tweet.text.replace('\n',''),tweet.favorite_count])
    df = pd.DataFrame(tweet_data,columns=columns_name)
    df.to_excel('tw_%s.xlsx'%tw_id, sheet_name='Sheet1')

    print("end")
get_tweets()
