#Getting all the tweets of a user using tweepy
#Twitter gives only access to the recet 3240 tweets

import tweepy 
import csv

#Twitter API credentials

consumer_key = "pf2lEelcb7JMXCKElmCYh1mPX"
consumer_secret = "S8NabhiuhUaH9zE3qd7fLtQ4TkoPA8kjY37AZKuPAGysYxlKfn"
access_key = "1145587541904515072-c7lDuXwmHgbUvix5x6i0PHXtaejkFj"
access_secret = "AyhlxWGYpcVBRSnu7lJJKlcIIHdtlfBdd8ITHwK34Q4rA"


def get_all_tweets(screen_name):
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		#print ("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		#print ("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	username = input("Enter the user name without @ :")
    
	get_all_tweets(username)
