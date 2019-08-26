# Analysis on tweets using Vader algorithm
import pandas as pd
import sys,csv,re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import os

class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def DownloadData(self):
        
                
        searchTerm = username
        NoOfTerms = len(data['text'])
        self.tweets = data['text']
       

        # creating some variables to store info
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0
        
        analyser = SentimentIntensityAnalyzer()
        polarities =[]

        # iterating through tweets fetched
        for tweet in self.tweets:
           
            score = analyser.polarity_scores(tweet)
            polarities.append(score['compound'])  # Append each tweet's polarity to a list
            polarity += score['compound']  # adding up polarities to find the average later
            
            if (score['compound'] == 0):  # adding reaction of how Modi is reacting to find average later
                neutral += 1
            elif (score['compound'] > 0 and score['compound'] <= 0.3):
                wpositive += 1
            elif (score['compound'] > 0.3 and score['compound'] <= 0.6):
                positive += 1
            elif (score['compound'] > 0.6 and score['compound'] <= 1):
                spositive += 1
            elif (score['compound'] > -0.3 and score['compound'] <= 0):
                wnegative += 1
            elif (score['compound'] > -0.6 and score['compound'] <= -0.3):
                negative += 1
            elif (score['compound'] > -1 and score['compound'] <= -0.6):
                snegative += 1

        df = data
        df['polarity'] = polarities
        export_csv = df.to_csv (r'%s_tweets_with_polarity.csv' % username, index = True, header=True)

        # finding average of how people are reacting
        positive = self.percentage(positive, NoOfTerms)
        wpositive = self.percentage(wpositive, NoOfTerms)
        spositive = self.percentage(spositive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        wnegative = self.percentage(wnegative, NoOfTerms)
        snegative = self.percentage(snegative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)
        
       
        # finding average reaction
        polarity = polarity / NoOfTerms

        # printing out data
        print("Analysis of " + username, str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")

        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")

        print()
        print("Detailed Report: ")
        print(str(positive) + "% tweets were positive")
        print(str(wpositive) + "% tweets were weakly positive")
        print(str(spositive) + "% tweets were strongly positive")
        print(str(negative) + "% tweets were negative")
        print(str(wnegative) + "% tweets were weakly negative")
        print(str(snegative) + "% tweets were strongly negative")
        print(str(neutral) + "% tweets were neutral")

        self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, NoOfTerms)


    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    def plotPieChart(self, positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
        sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
        colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('Persona by using his recent ' + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()



if __name__== "__main__":
    sa = SentimentAnalysis()
    sa.DownloadData()
