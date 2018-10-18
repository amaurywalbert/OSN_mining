import operator,json, re
from collections import Counter
from nltk.corpus import stopwords
from nltk import bigrams
import string

emoticons_str = r"""
	(?:
		[:=;] # Eyes
		[oO\-]? # Nose (optional)
		[D\)\]\(\]/\\OpP] # Mouth
	)"""
 
regex_str = [
	emoticons_str,
	r'<[^>]+>', # HTML tags
	r'(?:@[\w_]+)', # @-mentions
	r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
	r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
	
	r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
	r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
	r'(?:[\w_]+)', # other words
	r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
	return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
	tokens = tokenize(s)
	if lowercase:
		tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
	return tokens

punctuation = list(string.punctuation)
stop = stopwords.words('portuguese') + punctuation + ['rt', 'via']

fname = 'data/test.json'
with open(fname, 'r') as f:
	count_all = Counter()
	count_stop = Counter()
	count_single = Counter()
	count_hash = Counter()
	count_only = Counter()
	count_bigram = Counter()
	for line in f:
		tweet = json.loads(line)
		terms_all = [term for term in preprocess(tweet['text'])]	# Create a list with all the terms
		terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
		terms_single = set(terms_all)					# Count terms only once, equivalent to Document Frequency
		terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]	# Count hashtags only
		terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))] # Count terms only (no hashtags, no mentions)
		terms_bigram = bigrams(terms_stop)	
 
		count_all.update(terms_all)				 # Update the counter for all terms
		count_stop.update(terms_stop)				 # Update the counter for terms in not stopwords
		count_single.update(terms_single)		 # Update the counter for terms count once
		count_hash.update(terms_hash)				 # Update the counter for terms hashtag
		count_only.update(terms_only)				 # Update the counter for terms in not hashtag and mention 
		count_bigram.update(terms_bigram)		 # Update the counter for terms in not hashtag and mention

	print(count_all.most_common(5))		    	# Print the first 5 most frequent words
	print(count_stop.most_common(5))		    	# Print the first 5 most frequent words
	print(count_single.most_common(5))		   # Print the first 5 most frequent words
	print(count_hash.most_common(5))		    	# Print the first 5 most frequent words
	print(count_only.most_common(5))		    	# Print the first 5 most frequent words
	print(count_bigram.most_common(5))	    	# Print the first 5 most frequent words


# mind the ((double brackets))
# startswith() takes a tuple (not a list) if 
# we pass a list of inputs