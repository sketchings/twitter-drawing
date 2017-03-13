import json
import datetime
import random
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/tweets_save.txt') as tweetfile:
    tweets = json.load(tweetfile)

action = input("what would you like to do? ")
retweet = input("would you like retweets? [y/n] ")
howmany = input("how many would you like to see? [all/x] ")

create_fmt = '%a %b %d %H:%M:%S %z %Y'
input_fmt = '%m/%d/%Y %z'
usetweets = []
if action == "range":
    start = input("enter start date? (mm/dd/yyyy) ")
    end = input("enter end date? (mm/dd/yyyy) ")
    start_date = datetime.datetime.strptime(start+' +0000',input_fmt)
    end_date = datetime.datetime.strptime(end+' +0000',input_fmt)

if action == 'all' and retweet == 'y':
    usetweets = tweets
else:
    for tweet in tweets:
        if action == 'all':
            if 'retweeted_status' not in tweet:
                usetweets.append(tweet.copy())

        if action == "range":
            created = datetime.datetime.strptime(tweet["created_at"],create_fmt)
            if created >= start_date and created <= end_date:
                if retweet == 'y' or 'retweeted_status' not in tweet:
                    usetweets.append(tweet.copy())

        if action == "treehouse":
            people = [
                'sketchings',
                'benjakuben',
                'patrickbells',
                'davemcfarland',
                'kenwalger',
                'craigsdennis',
                'ryancarson',
                'EmSchw',
                'SmashDev',
                'treasureporth',
                'mattzyzy',
                'pajamatron',
                'sfgergasi',
                'kennethlove',
                'e9dorf',
            ]
            if tweet['user']['screen_name'] in people:
                if retweet == 'y' or 'retweeted_status' not in tweet:
                    usetweets.append(tweet.copy())

if howmany == 'all':
    for tweet in usetweets:
        print(tweet['user']['screen_name'] + ' : ' + tweet['text'])
else:
    count = 0
    while count < int(howmany):
        count = count + 1
        tweet = random.choice(usetweets)
        print(tweet['user']['screen_name'] + ' : ' + tweet['text'])

print('Total: ')
print(len(usetweets))
