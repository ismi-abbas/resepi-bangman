import tweepy
import time
import pandas as pd

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)


username = "@aimansalim_"
no_of_tweets = 10

try:
    # The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)

    # Pulling Some attributes from the tweet
    attributes_container = [
        [tweet.created_at, tweet.favorite_count, tweet.source, tweet.text]
        for tweet in tweets
    ]

    # Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]

    # Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print("Status Failed On,", str(e))
    time.sleep(3)
