import tweepy
from tweepy import OAuthHandler
from authentication import get_twitter_client

api = get_twitter_client()

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)		# Process a single status
