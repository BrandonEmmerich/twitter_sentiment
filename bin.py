import private
import settings
import tweepy
import web

# Open Twitter API -------------------------------------------------------------
auth = tweepy.OAuthHandler(private.CONSUMER_KEY, private.CONSUMER_SECRET)
auth.set_access_token(private.ACCESS_TOKEN_KEY, private.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Open listener ----------------------------------------------------------------
stream_listener = web.StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=settings.TRACK_TERMS)
