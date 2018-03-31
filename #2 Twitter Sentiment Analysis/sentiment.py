from textblob import TextBlob
import tweepy

wiki=TextBlob("bad worth the worest kill ")
print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)

consumer_key = "u7JeQD9886p1Uu3qdZxL5HqGt"
consumer_secret = "W6qxJZLg3dndms5Kd4frJZ3ZDjkYIYZseMx3jk4XzkzNtlFf82"

access_token = "2800575616-FsgteWeoet94LmkRl913vc7tmg4Nue9Wnss1fBx"
access_token_secret	= "bBGtheePo8fg6gjWVrvwsruGHmLJWvCl219nF6lhFbQLk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api=tweepy.API(auth)

public_tweents= api.search('Trump')

for tweet in public_tweents:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)