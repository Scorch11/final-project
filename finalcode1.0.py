pip install tweepy

from tweepy import OAuthHandler
from tweepy import API
import pandas as pd
import matplotlib.pyplot as plt

CONSUMER_KEY = 'rgfd0QcdXsJtIWXn6iPS69lzn'
CONSUMER_SECRET = 'XogXQDd6hPafh8LNx5Bmrz2s2rrDaZJt6BFQOnQi9p2HhyBqPH'
OAUTH_TOKEN = '1485025684619612161-F5QdT8xz9Wdmk2lRBvCdVdL3WtaXVj'
OAUTH_TOKEN_SECRET = 'dCm3U5Udb6yLwGTnYWoXAlsdvLJPeVDPXIyNxrhTQKnZ1'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = API(auth, wait_on_rate_limit=True)

account_list = ["UarizonaCAST", "NAU"]
if len(account_list) > 0:
    for target in account_list:
        print("Getting data for " + target)
        item = api.get_user(screen_name=target)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)

tweetscopy = []


def UsersHashtags(screenname):
    item = api.get_user(screen_name=screenname)
    searchQList = ["#BLM", "#VetransDay", "#SucidedAwareness", "#SaveTheTrees"]
    tweets = item.search_tweets(query=searchQList, lang="en", since="2020-09-16").items(50)
    for tweet in tweets:
        tweetscopy.append(tweet)
    print("Total Tweets fetched:", len(tweetscopy))


tweetinfo = []


def TweetInformation():
    for tweet in tweetscopy:
        tweetInfo = {
            'created_at': tweet.created_at,
            'text': tweet.text,
            'source': tweet.source,
            'name': tweet.name,
            'username': tweet.username,
            'location': tweet.location,
            'verified': tweet.verified,
            'description': tweet.description}
        tweetinfo.append(tweetInfo)


def StackedBar():
    for tweets in tweetscopy:
        ax = plt.subplots()
        ax.bar(tweets)


UsersHashtags("UarizonaCAST")
UsersHashtags("NAU")
tweetDataFrame = pd.DataFrame(tweetinfo)
tweetDataFrame.head()
StackedBar()



#this next secion is all my code for the graph and what not.
import random
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
#data = pd.read_table('finaldata1.0.py', delimiter='\t')
#df = pd.read_csv("finaldata1.0.csv")
#df = pd.DataFrame(data)
#print(df[['school', 'hashtags']])
def getData(fileName):
    dataFile = open(fileName, 'r')
    name = []
    school = []
    hashtags = []
   # for line in infile:
    #    name, school, hashtags = line.split(",")
    dataFile.readline() #discard header
    for line in dataFile:
        d, m = line.split(',')
        school.append(float(d))
        hashtag.append(float(m))
    dataFile.close()
    return (CarbonDioxide, Year)
    
def labelPlot():
    plt.title('data')
    plt.ylabel("school")
    plt.xlabel("hashtags")
    plt.zlabel("name")
    

def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = np.array(xVals)
    yVals = np.array(yVals)
 
    plt.plot(yVals, xVals, 'bo',
               label = 'Measured displacements')
    labelPlot()
    plt.show()
    
plotData('finaldata1.0.csv')
