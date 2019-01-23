import psycopg2
import private
import settings
import time
import tweepy
from urllib3.exceptions import ProtocolError


class StandardListner(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

        try:
            cur = conn.cursor()
            data = status._json

            row = {
                'tweet_created_at': time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(data['created_at'],'%a %b %d %H:%M:%S +0000 %Y')),
                'tweet_favorite_count': data['favorite_count'],
                'tweet_id': data['id'],
                'tweet_language': data['lang'],
                'tweet_place': data.get('place'),
                'tweet_retweet_count': data['retweet_count'],
                'tweet_text': data['text'],
                'tweet_timestamp': int(data['timestamp_ms']),
                'user_created_at': data['user'].get('created_at'),
                'user_description': data['user'].get('description'),
                'user_favourites_count': data['user'].get('favourites_count'),
                'user_friends_count': data['user'].get('friends_count'),
                'user_id': data['user'].get('id'),
                'user_location': data['user'].get('location'),
                'tweet_full_text': None,
            }

            if data['truncated']:
                dict_full_text = {
                    'tweet_full_text': data['extended_tweet']['full_text'],
                }
                row.update(dict_full_text)

            cur.execute(settings.QUERY_INSERT, row)
            conn.commit()

        except Exception as e:
            conn.rollback()
            print e

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    with psycopg2.connect(private.AWS_CONNECTION_STRING) as conn:

        listener = StandardListner()
        auth = tweepy.OAuthHandler(private.CONSUMER_KEY, private.CONSUMER_SECRET)
        auth.set_access_token(private.ACCESS_TOKEN_KEY, private.ACCESS_TOKEN_SECRET)
        stream = tweepy.Stream(auth, listener)
        while True:
            try:
                stream.filter(track=settings.SEARCH_TERMS)
            except ProtocolError:
                continue
