import tweepy as tw
api_key = 'xxxxxxxxxxxxxxxxxxx'
api_secret = 'xxxxxxxxxxxxxxxx'

auth = tw.OAuthHandler(api_key,api_secret)
api = tw.API(auth)


searchQ = "#BLM -filter:retweets"
tweets = api.search_tweets (q=searchQ, lang="en",since="2020-09-16").items(50)
# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)

print("Total Tweets fetched:", len(tweets_copy))