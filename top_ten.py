import urllib
import json
import sys
import operator

def main():
	tweet_file = open(sys.argv[1])

	tweet_lines = tweet_file.readlines()

	top_ten={}
	line =0
	for t in tweet_lines:
		tweet = json.loads(t)
		sentiment=0.0
		if(tweet.has_key('entities')):
			hashtags=tweet['entities']['hashtags']
			for hashtag in hashtags:
				h=hashtag['text']
				if (top_ten.has_key(h)):
					top_ten[h]+=1
				else:
					top_ten[h]=1
		


	sorted10=sorted(top_ten.iteritems(),key=lambda (k,v):(v,k),reverse=True)[:10]
	for key in sorted10:
                print key[0],key[1]*1.0

				
	tweet_file.close()

if __name__ == '__main__':
    main()
