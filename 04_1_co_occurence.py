import operator,json, re, string
from collections import Counter
from nltk.corpus import stopwords
from nltk import bigrams
from collections import defaultdict

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
	count_only = Counter()
	com = defaultdict(lambda : defaultdict(int))
 
	for line in f:
		tweet = json.loads(line)
		terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))]
 
	for i in range(len(terms_only)-1):	# Build co-occurrence matrix            
		for j in range(i+1, len(terms_only)):
			w1, w2 = sorted([terms_only[i], terms_only[j]])                
			if w1 != w2:
				com[w1][w2] += 1	
	
	com_max = []
	for t1 in com:	# For each term, look for the most common co-occurrent terms
		t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
		for t2, t2_count in t1_max_terms:
			com_max.append(((t1, t2), t2_count))

	terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)	# Get the most frequent co-occurrences
	print(terms_max[:5])