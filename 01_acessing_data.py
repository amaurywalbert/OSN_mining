import tweepy
from tweepy import OAuthHandler
 
consumer_key = '9CVrUgUL1ztECIpEEHQyg7s9B'
consumer_secret = 'NJj7XUOO7WuR9AmdjY5BwFD6PUIBe89zXaU52IfHvJnEhtLCA6'
access_token = '1052708465871851523-pX9YVeCnYQOeVCwsUrdDu3IX23Fpxt'
access_secret = 'u9XagzYWw0yuiJAuFqPQapofBhFoivSugKeXYl6D0Xlpk'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

