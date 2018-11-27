## tweets.py
# Dean Mock / Theo Stumpf
## Version 22 Nov 2018

# Accessing the Twitter API
# This script describes the basic methodology for accessing a Twitter feed
# or something similar.

# Loading libraries needed for authentication and requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import json
import urllib
import main.py
from pprint import pprint

# In order to use this script, you must:
# - Have a Twitter account and create an app
# - Store in keys.json a property called "twitter" whose value is an
#     object with two keys, "key" and "secret"
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['twitter']

twitter_key = keys['key']
twitter_secret = keys['secret']

# We authenticate ourselves with the above credentials
# We will demystify this process later
#
# For documentation, see http://requests-oauthlib.readthedocs.io/en/latest/api.html
# and http://docs.python-requests.org/en/master/
client = BackendApplicationClient(client_id=twitter_key)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://api.twitter.com/oauth2/token',
                          client_id=twitter_key,
                          client_secret=twitter_secret)

# Base url needed for all subsequent queries
base_url = 'https://api.twitter.com/1.1/'

# Particular page requested. The specific query string will be
# appended to that.
page = 'search/tweets.json'

# function converting user input text to URL
def encodeTitle(movie_title):
	url_title = urllib.parse.urlencode(movie_title)
	#or just url_title = urllib.urlencode(movie_title)
	return url_title


# Depending on the query we are interested in, we append the necessary string
# As you read through the twitter API, you'll find more possibilities
### Change this from Hanover College to user input "movie title"
#req_url = base_url + page + '?q=Hanover+College&tweet_mode=extended&count=100'

### Perhaps this? Double check this with Theo or Skiadas
def getURL(url_title):
	req_url = base_url + page + '?q=' + url_title + '&tweet_mode=extended&count=100'
	return req_url

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

## Process the results
## CAUTION: The following code will attempt to read up to 10000 tweets that
## Mention Hanover College. You should NOT change this code.
tweets = results['statuses']
while True:
   if not ('next_results' in results['search_metadata']):
      break
   if len(tweets) > 10000:
      break
   next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
   print(results['search_metadata']['next_results'])
   response = oauth.get(next_search)
   results = json.loads(response.content.decode('utf-8'))
   tweets.extend(results['statuses'])

## CAUTION: For the rest of this assignment, the list "tweets" contains all the
## tweets you would want to work with. Do NOT change the list or the value of "tweets".

#####below here write the list comprehension code. then youre gonna want to run this program in the Python terminal

###tweets

texts = [text['full_text'] for text in tweets]
print(texts)

## hashtags

def get_hashtags(tweet):
	hash_list = []
	hashtags = tweet['entities']['hashtags']
	for tag in hashtags:
		hash_list.append(tag['text'])

	return(hash_list)

tags_per_tweet = [get_hashtags(tweet) for tweet in tweets]
	
print(tags_per_tweet)