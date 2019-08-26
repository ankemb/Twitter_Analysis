#Get the total number of tweets, friends count and number of followers of a particular User, aong with latest 10 tweets
#and also provide the friends names alog with followers names
import requests
from requests_oauthlib import OAuth1

 
screen_name = input("Enter the twitter handle without @ :") ###Twitter handle

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json' ### url to Twitter API for user time line

pms = {'screen_name' : screen_name, 'count' : 10, 'lang' : 'en'} ### parameters according to Twitter API, max of 100 tweets


consumer_key = "pf2lEelcb7JMXCKElmCYh1mPX"
consumer_secret = "S8NabhiuhUaH9zE3qd7fLtQ4TkoPA8kjY37AZKuPAGysYxlKfn"
access_token = "1145587541904515072-c7lDuXwmHgbUvix5x6i0PHXtaejkFj"
access_token_secret = "AyhlxWGYpcVBRSnu7lJJKlcIIHdtlfBdd8ITHwK34Q4rA"
    
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)	
 
res = requests.get(url, params=pms, auth=auth)

tweets1 = res.json()

Name = tweets1[0]['user']['name']
Screen_name = tweets1[0]['user']['screen_name']
tn_tweets = tweets1[0]['user']['statuses_count']
tn_friends = tweets1[0]['user']['friends_count']
tn_followers = tweets1[0]['user']['followers_count']

print ('Name:',Name,'\tScreen name:',Screen_name)
print ('Total Number of Tweets:',tn_tweets)
print ('Total Number of Friends:',tn_friends)
print ('Total Number of Followers:',tn_followers)

print('Latest Tweet created at:',tweets1[0]['created_at'])

if tn_tweets > 10:
    print ('Latest 10 tweets:')
    i = 0
    for i in range(10):
        print('Tweet',i,':',tweets1[i]['text'])
        i = i+1
    
else:
    print('All tweets:')
    i = 0
    for i in range(tn_tweets):
        print('Tweet',i,':',tweets1[i]['text'])
        i = i+1


# Getting the friends names

url = 'https://api.twitter.com/1.1/friends/ids.json' ### url to Twitter API

pms = {'screen_name' : screen_name, 'count':99, 'lang' : 'en'} ### parameters according to Twitter API, max of 100 tweets

 
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)	
 
res = requests.get(url, params=pms, auth=auth)

tweets1 = res.json()

user_ids = tweets1['ids']

url = 'https://api.twitter.com/1.1/users/lookup.json'
    
pms = {'screen_name' : screen_name, 'user_id' : user_ids, 'lang' : 'en'}

res = requests.get(url, params=pms, auth=auth)

tweets2 = res.json()
length = len(tweets1['ids'])
print('Sample list of Friends max of 100:')
i = 0
for i in range(length):
    print(tweets2[i]['name'])
    i = i + 1

# Getting the followers names

url = 'https://api.twitter.com/1.1/followers/ids.json' ### url to Twitter API

pms = {'screen_name' : screen_name, 'count' :99,  'lang' : 'en'} ### parameters according to Twitter API, max of 100 tweets


consumer_key = "pf2lEelcb7JMXCKElmCYh1mPX"
consumer_secret = "S8NabhiuhUaH9zE3qd7fLtQ4TkoPA8kjY37AZKuPAGysYxlKfn"
access_token = "1145587541904515072-c7lDuXwmHgbUvix5x6i0PHXtaejkFj"
access_token_secret = "AyhlxWGYpcVBRSnu7lJJKlcIIHdtlfBdd8ITHwK34Q4rA"
    
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)	
 
res = requests.get(url, params=pms, auth=auth)

tweets1 = res.json()

user_ids = tweets1['ids']


url = 'https://api.twitter.com/1.1/users/lookup.json'
    
pms = {'screen_name' : screen_name, 'user_id' : user_ids, 'lang' : 'en'}

res = requests.get(url, params=pms, auth=auth)

tweets2 = res.json()


length = len(tweets1['ids'])
print('Sample list of followers max of 100:')
i = 0
for i in range(length):
    print(tweets2[i]['name'])
    i = i + 1
