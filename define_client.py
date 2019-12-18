# --------------------------------------------------------------------
#   define_client.py
#
#                   Apr/26/2019
# --------------------------------------------------------------------
import os
from dotenv import load_dotenv
from os.path import join, dirname
from requests_oauthlib import OAuth1Session
import oauth2 as oauth
# --------------------------------------------------------------------
def define_client_proc():
    #dotenv_path = '.env'
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
#
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
    client = oauth.Client(consumer, access_token)
#
    return client
# --------------------------------------------------------------------
