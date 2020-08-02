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


# consumer_key="K7dHcWL94je6OqIFXFANPtxei"
# consumer_secret="9Y14t2et6OmLUdXI14KUfUoGnKl5uzTeisTrMG1bHhSUZ4VJAK"
# access_token="1063443082992066561-4hz7NTsrSBISbAUwvsBoNBUdwg5bmD"
# access_token_secret="E5j4DDqXjrrOrrvbY4YDIxh0heJCpxC7rFEEZVdvtJ3R7"

# consumer_key2="qxE2h8gsxiRKxhBji3qtALfW1"
# consumer_secret2="LcqRdZGml2Th9yRGSW1OcV0bhG6AN5g3o6wW72Ra70WCtJHMxv"
# access_token2="1063443082992066561-6OTM7AACJhKPJ0OTMdeOvnlX2DrLMZ"
# access_token_secret2="ooyl84dnKUDgt0CnfbBQlWhF0VvuLvci3V0Z94llyD8wI"

# consumer_key="UwMox6N9xrdVcY5hZvZGBLelJ"
# consumer_secret="privea4gPdlkn7JfXKYzxHDCmDbVYNUZrc9Mn3YVpg1FkdIlPI"
# access_token="1063443082992066561-6TcWY4LzY21iGswNsEgDJgvLjBLE5H"
# access_token_secret="oFPx6OW1eO7RswYD4DpMJ3bA4vFXWpufL85xCLNbk9SaD"

# consumer_key="pxBKWrfEXRJjOYfSI35VDp3Cj"
# consumer_secret="D2djgEfkFktKjDvx1Z3EOJqsTPzdiHaX9iqqoIqvIjz3BDhqgq"
# access_token="1063443082992066561-bg4Z4diMRFXc6OMLOrDh3b7XqQuF4N"
# access_token_secret="m5cQFLV23meXq8lxbaIc21arj8jfNHOyCTAMLd9XC0Tev"

# consumer_key="xITAF3eKITbF4L9PqRnNsF43t"
# consumer_secret="Jj2nGRBJnCLcojVR5YSvBdjsgQTdGUXFU3i1HoW4LKd71wx6vD"
# access_token="1063443082992066561-2A6Fr13CdloYDqV0ID1J5yki5h2z8T"
# access_token_secret="O6fsawfAALlL08HXLBhnMEgC3O9HlVeK1Eqsc4Zru39bq"

consumer_key="LhNkkGjmugupq1sxtMwCjKw4L"
consumer_secret="HEqD6gnTZWFkUNgNBHPvSRlCYVbBLcCWIML9QWmalA40f4424C"
access_token="1063443082992066561-JVsH7joANNYvDatpXkWI4AmCkKM2xw"
access_token_secret="2K2XXJ3ljSBf13StwVnGxxkHlGc7KWoCrraB5zYX8aDB4"

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

        









