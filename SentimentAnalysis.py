import tweepy
from textblob import TextBlob

class tweet_handler(object):
    def __init__(self):
        consumer_key = '##'
        consumer_secret = '##'
        access_token = '##'
        access_token_secret = '##'
        try:
            self.auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
            self.auth.set_access_token(access_token,access_token_secret)
            self.api=tweepy.API(self.auth)
            #api.update_status('tweepy + oauth!')
        except:
            print("Error: Authentication Failed")


    def get_tweet_sentiment(self,tweet):
         test_tweet = TextBlob(tweet)
         if test_tweet.sentiment.polarity>0:
             return "positive"
         elif test_tweet.sentiment.polarity ==0:
             return "neutral"
         else:
             return "negative"
            
                

    def get_tweets(self,query,count=10):
        tweets=[]
        try:
            fetched_tweets=self.api.search(q=query,count=count)
            for tweet in fetched_tweets:
                parsed_tweets={}
                parsed_tweets['text']=tweet.text
                parsed_tweets['sentiment']=self.get_tweet_sentiment(tweet.text)
                if tweet.retweet_count>0:
                    if parsed_tweets not in tweets:
                        tweets.append(parsed_tweets);
                else:
                    tweets.append(parsed_tweets);                    
            return tweets
        except tweepy.TweepError as e:
            print("error : "+str(e))     



def main():
    obj=tweet_handler()
    tweets=obj.get_tweets(query="kerala flood",count=20)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    print("\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
    print("---------------------------------------------------------------------")
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    print("\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])



        
if __name__ == "__main__":
    # calling main function
    main()
        
        
        
