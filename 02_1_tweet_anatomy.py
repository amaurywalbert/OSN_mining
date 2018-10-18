import json
 
with open('data/test.json', 'r') as f:
	for line in f.readlines():
		tweet = json.loads(line) # load it as Python dict
		print(json.dumps(tweet, indent=4)) # pretty-print
		print
