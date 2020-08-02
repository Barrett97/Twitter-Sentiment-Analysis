"""
    This script connects to Twitter Streaming API, gets tweets with '#' and
    forwards them through a local connection in port 9009. That stream is
    meant to be read by a spark app for processing. Both apps are designed
    to be run in Docker containers.

    To execute this in a Docker container, do:
    
        docker run -it -v $PWD:/app --name twitter -p 9009:9009 python bash

    and inside the docker:

        pip install tweepy
        python twitter_app.py

    For more instructions on how to run, refer to final slides in tutorial 8

    Made for: EECS 4415 - Big Data Systems (York University EECS dept.)
    Author: Tilemachos Pechlivanoglou

"""

import socket
import sys
import json
import re
import csv
import tweepy
import time

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy import Stream

consumer_key=
consumer_secret=
access_token=
access_token_secret=

# ==== setup twitter connection ====
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
batch = API(auth)

language = ['en']
qtrack = 'mentalhealth OR mentalillness OR mental health OR mental illness OR depression OR depressed OR anxiety OR anxious OR stress OR nostigma OR presspause OR addiction OR endthestigma OR trauma OR suicide OR shellshock OR operationalstress OR alcoholism OR ptsd OR bipolar OR mhsm OR bpd'

print(batch.rate_limit_status()['resources']['search']['/search/tweets'])

with open('1129.csv', 'w+') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for tweet in Cursor(batch.search,
                        count=100,
                        tweet_mode='extended',
                        q=qtrack,
                        since="2018-11-29", # search starting from morning to midnight of 'since' date
                        until="2018-11-30", # can't start search from the middle of the day
                        lang="en").items():
        if not tweet.full_text[0] == 'R' and  not tweet.full_text[1] == 'T': # exclude retweets
            writer.writerow([tweet.created_at, tweet.full_text, tweet.favorite_count, tweet.retweet_count, tweet.id, tweet.user.screen_name])

        









