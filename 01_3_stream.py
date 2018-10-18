from tweepy import Stream
from tweepy.streaming import StreamListener
from authentication import get_twitter_auth

auth = get_twitter_auth()

class MyListener(StreamListener):
 
	def on_data(self, data):
		try:
			with open('data/eleicoes.json', 'a') as f:
				f.write(data)
				print(data)
				print
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True
 
	def on_error(self, status):
		print(status)
		return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#bolsonaro', '#haddad'])
