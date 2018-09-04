import tweepy
from textblob import TextBlob

# You will need a twitter developer account in order to interface with the api
# see the tweepy docs for more information on interfacing with the twitter api

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Getting user input
phrase = input("Enter a search string: ")
public_tweets = api.search(phrase, count=100)

# Analysing each tweets polarity
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity

# Determineing averages
tweets = [TextBlob(tweet.text) for tweet in public_tweets]
rating = [TextBlob(tweet.text).sentiment.polarity for tweet in public_tweets]

avg = sum(rating) / len(rating)

# printing results based on thresholds
if avg > 0.2:
    print("The last 100 tweets regarding " + phrase + " were positive")
elif avg < 0.2:
    print("The last 100 tweets regarding " + phrase + " were negative")
else:
    print("The last 100 tweets regarding " + phrase + " were neutral")


