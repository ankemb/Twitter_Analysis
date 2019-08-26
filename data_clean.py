#Clean the data
import pandas as pd #Import pandas for data frames
import re,ast,csv

name= username +'_tweets.csv'

data = pd.read_csv(name)
data['text'] = data['text'].apply(ast.literal_eval).str.decode("utf-8")
df =[]

for line in data['text']:
    x = re.sub(r'http\S+', '', line)#match http followed by nonspace and replace with empty string using Regular expression
    df.append(x)


    
data['text']=df
