#!/usr/bin/python2

import tweepy

consumer_key = "R1oEqLXen76cFW5kuhni9Fk2b" 
consumer_secret = "BrGEhhsImRZ7CXG9Szxq1xTddbhK5BziiKvt1mW4rh6aZi0sJ4"
access_key = "954782399480516609-FqvlB6JDiFXolwRkOebGNCnLKdGn0nE"
access_secret = "QwW00MLvgTBMfLI43d2mD3ChoqPdkfKfYd77tfRuvbQCH"
  
# Function to extract tweets 
def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=20
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        print(tmp) 
  
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("@imVkohli")  
