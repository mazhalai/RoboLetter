import urllib
import json
import sys


def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	afinnfile = sent_file.readlines()
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	tweet_lines = tweet_file.readlines()

	happy_state={}
	for t in tweet_lines:
		tweet = json.loads(t)
		sentiment=0.0
		if(tweet.has_key('text')):
			tweet_text=tweet['text']
			tweet_words = tweet_text.split(' ')
			for word in tweet_words:
				if word in scores:
					sentiment+=scores[word]
					place = tweet['user']['location'].split()
					for p in place:
						if (len(p)==2):
							if (happy_state.has_key(p) or happy_state.has_key(p.upper())):
								happy_state[p.upper()]+=1
							else:
								happy_state[p.upper()]=1

	print max(happy_state,key=happy_state.get)
				
	tweet_file.close()
	sent_file.close()

if __name__ == '__main__':
    main()
