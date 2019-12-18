#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
#   get_tweet.py
#
#                       Dec/21/2017
# --------------------------------------------------------------------
import sys
import json
import oauth2 as oauth
#
from define_client import define_client_proc
import html
import sys,io

# --------------------------------------------------------------------
# [8]:
def get_tweets_proc(client,user_id):
    nnx = 10
    url_base = "https://api.twitter.com/1.1/statuses/user_timeline.json?user_id="
    url = url_base + user_id + "&count=" + str(nnx)
    array_aa = []
    print(url)
    response, data = client.request(url)
    if response.status == 200:
        json_str = data.decode('utf-8')
#       print(json_str)
        array_aa = json.loads(json_str)
        sys.stderr.write("len(array_aa) = %d\n" % len(array_aa))
#
    else:
        sys.stderr.write("*** error *** get_ids_proc ***\n")
        sys.stderr.write("Error: %d\n" % response.status)
#
    return  array_aa
# --------------------------------------------------------------------
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # UTF-8に
sys.stderr.write("*** 開始 ***\n")

#
user_id = "frags_ruiz"
#
client = define_client_proc()
#
array_aa = get_tweets_proc(client,user_id)
#
sys.stderr.write("len(array_aa) = %d\n" % len(array_aa))
#
for unit_aa in array_aa:
    print (unit_aa['created_at'])
    print (unit_aa['id'])
    print (unit_aa['text'])
#
sys.stderr.write("*** 終了 ***\n")
# --------------------------------------------------------------------
