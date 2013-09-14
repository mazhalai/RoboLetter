import urllib
import json
import sys
from pprint import pprint,pformat


def main():
	tweet_file = open(sys.argv[1])

	tweet_lines = tweet_file.readlines()
	newdict={}
	for t in tweet_lines:
		tweet = json.loads(t)
		sentiment=0.0
		if(tweet.has_key('text')):
			tweet_text=tweet['text']
			tweet_words = tweet_text.split()
			for word in tweet_words:
				for newword in tweet_words: 
					if newword not in newdict:
						newdict[newword]=1.0
					else:
						newdict[newword]+=1.0
	size=len(newdict)
	for key in sorted(newdict.keys()):
    		print key, newdict[key]/size
	tweet_file.close()

if __name__ == '__main__':
    main()
