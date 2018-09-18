import private
import psycopg2
import settings
import time
import tweepy


run_id = str(int(time.time()))
conn = psycopg2.connect(private.CONNECTION_STRING)
insert_query = settings.QUERY_INSERT

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

        try:
            cur = conn.cursor()

            row = {
                'run_id': run_id,
                'id_str' : status.id_str,
                'user_screen_name' : status.user.screen_name,
                'user_created_at' : status.user.created_at,
                'user_location' : status.user.location,
                'user_description' : status.user.description,
                'user_followers' : status.user.followers_count,
                'tweet_date' : status.created_at,
                'tweet_text' : status.text
                }

            cur.execute(insert_query, row)
            conn.commit()

        except Exception as e:
            conn.rollback()
            print e


    def on_error(self, status_code):
        if status_code == 420:
            return False
