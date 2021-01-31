##### TWITTER_BOT #####
#######################


##########################
# Step 1: Import Packages
##########################

import tweepy
import time

#########################
# Step 2: Add Keys
#########################

#NB NB - ensure you leave no spaces in the text strings

# first add API key
# then add API secret key as second string

auth = tweepy.OAuthHandler('#APIKEY','#APISECRET')

# add Access Token
# then Access Token secret as second string
auth.set_access_token('#ACESSTOKEN','#ACCESSTOKENSECRET')

# ensure no ban ;)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True) 



##########################
# Step 3: Create a Cursor
##########################

user = api.me()

# replace #DataScience with the hashtag of your choosing
search = "#DataScience"
nr_Tweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nr_Tweets):
	try:
		tweet.favorite()
		tweet.retweet()
		print('Tweet Liked & Retweeted')
		time.sleep(15)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

