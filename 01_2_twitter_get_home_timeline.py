import tweepy, json
from tweepy import OAuthHandler
from authentication import get_twitter_client

api = get_twitter_client()

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    process_or_store(status._json)	    # Process a single status

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


