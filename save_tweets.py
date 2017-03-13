from config import *
import tweepy
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

json_api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
# If the authentication was successful, you should
# see the name of the account print out
#print(api.me().name)

with open(dir_path+'/tweets.txt') as tweetfile:
    try:
        tweets = json.load(tweetfile)
    except:
        not_set = True
    else:
        stop_id = tweets[0]['id']

while True:
    if 'last_id' in vars():
        results = json_api.search(q=search, max_id = last_id, count=100)
    elif 'stop_id' in vars():
        results = json_api.search(q=search, since_id = stop_id, count=100)
    else:
        results = json_api.search(q=search, count=100)

    count = len(results["statuses"])
    for num in range(0, count):
        if results["statuses"][num]['id'] == stop_id:
            results["statuses"] = results["statuses"][0:num-1]
            break


    if results["statuses"]:
        if 'last_id' in vars():
            if results["statuses"][-1]['id'] == last_id:
                break
        if 'combined' in vars():
            combined = combined + results["statuses"]
        else:
            combined = results["statuses"]
        last_id = results["statuses"][-1]['id']
    else:
        break

print(combined)
print('Added')
print(len(combined))
combined = combined + tweets
print('Brings us to a total of:')
print(len(combined))

file = open(dir_path+'/tweets.txt', 'w')
json.dump(combined, file, sort_keys=True, indent=4)
file.close()