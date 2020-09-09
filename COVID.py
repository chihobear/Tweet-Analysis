# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:05:34 2020

@author:
"""
import csv
import html
import datetime

try:
    import json
except ImportError:
    import simplejson as json

import sys
if sys.version_info[0] >= 3:
    unicode = str

import tweepy

class linkedList:
    def __init__(self, string):
        self.text = string
        self.next = None

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = "1188682490564595712-sz9CktFf0t1Yod6RvzndeIn1eaQKnQ"
ACCESS_SECRET = "TOhM04NOJB07Co8Eu9TCRS6vdCvl7RmAFf38TL6LGJHCF"
CONSUMER_KEY = "HxoKA5OfluA6qQYTxWD0sddT4"
CONSUMER_SECRET = "E7aNGkpgy2hwHFG7acowRwwvb2RLh4OTGhOeFQ2orCFdEGryir"

sleep_on_rate_limit=False

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

tweets_list = []
text_root = linkedList('')
def get_tweets(text_root, listOfTweets,keywords,numOfTweets):
    count = 0
    cur_node = text_root
    #for tweet in api.search(q = keywords, lang = "en", count = numOfTweets, tweet_mode="extended"):
    for tweet in tweepy.Cursor(api.search, q=keywords,granularity="country", query='USA', lang = 'en', tweet_mode='extended').items(numOfTweets):
        count += 1
        cur_node.next = linkedList('tweet' + str(count) + '\n' + str(tweet) + '\n\n\n')
        cur_node = cur_node.next
        dict_ = {'Screen Name': html.unescape(tweet.user.screen_name),
                'User Name': html.unescape(tweet.user.name),
                'Tweet Created At': unicode(tweet.created_at),
                'Tweet Text': None,
                'User Location': unicode(tweet.user.location),
                'Tweet Coordinates': unicode(tweet.coordinates),
              #  'Followers Count': unicode(tweet.user.followers_count),
                'Retweet Count': unicode(tweet.retweet_count),
                'Phone Type': unicode(tweet.source),
                'Favorite Count': unicode(tweet.favorite_count),
                'Favorited': unicode(tweet.favorited),
                'Replied': unicode(tweet.in_reply_to_status_id_str),
                'Followers Count': unicode(tweet.user.followers_count)
                }
        try:
            temp = html.unescape(tweet.retweeted_status.full_text)
            head = tweet.full_text[:tweet.full_text.index(':') + 2]
            dict_['Tweet Text'] = head + temp
        except AttributeError:
            dict_['Tweet Text'] = html.unescape(tweet.full_text)
        listOfTweets.append(dict_)
    return listOfTweets


#a = get_tweets(tweets_list,'COVID OR coronavirus OR #coronavirus OR #COVID',20000)
a = get_tweets(text_root, tweets_list,'COVID OR coronavirus OR #coronavirus OR #COVID\
                            OR Wuhan Virus OR WuhanVirus OR #WuhanVirus \
                           OR #ChinaVirus OR Chinese Virus OR #ChineseVirus', 5000)
date = datetime.datetime.now().strftime('%m-%d %H:%M')
#with open('COVID(' + date + ').json', 'w+', encoding='utf-8') as json:
with open('C:\\Users\\linan\\Desktop\\COVID data\\COVID.json', 'w+', encoding='utf-8') as json:
    temp = text_root.next
    while temp:
        json.write(temp.text)
        temp = temp.next
#with open('COVID(' + date + ').csv', 'w+', encoding='utf-8') as twitter:
with open('C:\\Users\\linan\\Desktop\\COVID data\\COVID.csv', 'w', newline='', encoding='utf-8') as twitter:
    writer = csv.writer(twitter)
    writer.writerow(['Screen Name', 'User Name', 'Tweet Created At', 'Tweet Text',
                     'User Location', 'Tweet Coordinates', 'Retweet Count',
                     'Phone Type', 'Favorite Count', 'Favorited', 'Replied', 'Followers Count'])
    for ele in a:
        writer.writerow([ele['Screen Name'], ele['User Name'], ele['Tweet Created At'], ele['Tweet Text'],
                     ele['User Location'], ele['Tweet Coordinates'], ele['Retweet Count'],
                     ele['Phone Type'], ele['Favorite Count'], ele['Favorited'], ele['Replied'], ele['Followers Count']])


