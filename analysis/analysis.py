import json
import pprint

tweets_data = []
tweets_file = open('twitter_data.txt', "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

pprint.pprint(tweets_data[100])

import ipdb; ipdb.set_trace()
