import urllib
import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	afinnfile = sent_file.readlines()
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	tweet_lines = tweet_file.readlines()

	for t in tweet_lines:
		tweet = json.loads(t)
		sentiment=0.0
		if(tweet.has_key('text')):
			tweet_text=tweet['text']
			tweet_words = tweet_text.split(' ')
			for word in tweet_words:
				if word in scores:
					sentiment+=scores[word]
		print sentiment
				
	tweet_file.close()
	sent_file.close()

if __name__ == '__main__':
    main()
