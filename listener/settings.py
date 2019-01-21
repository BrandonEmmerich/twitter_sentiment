SEARCH_TERMS = ["bumbler", "tinder", "coffee meets bagel", "jswipe"]

QUERY_INSERT = '''
    INSERT INTO twitter_sentiment.dating_apps
    (tweet_created_at, tweet_favorite_count, tweet_id, tweet_language,
    tweet_place, tweet_retweet_count, tweet_text, tweet_timestamp,
    user_created_at, user_description, user_favourites_count, user_friends_count,
    user_id, user_location, tweet_full_text)
    VALUES
    (%(tweet_created_at)s, %(tweet_favorite_count)s, %(tweet_id)s, %(tweet_language)s,
    %(tweet_place)s, %(tweet_retweet_count)s, %(tweet_text)s, %(tweet_timestamp)s,
    %(user_created_at)s, %(user_description)s, %(user_favourites_count)s, %(user_friends_count)s,
    %(user_id)s, %(user_location)s, %(tweet_full_text)s)
     '''
