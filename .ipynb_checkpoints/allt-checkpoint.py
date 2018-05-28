import tweepy
import csv
CONSUMER_KEY    = 'O1cU3FTzo7QcM0bwQzuM9MOZG'
CONSUMER_SECRET = 'lVrZEfNRSbkgIvGrXKccahIuKgkszdLebx21rJamw6ukb6Wt52'
ACCESS_TOKEN  = '941945158873915392-Gb0x45RTvnoTN5KIBfP0BP29ELAtUJc'
ACCESS_SECRET = 'EjuvEP0qCDwa6yKjB0aprGfdIzjxwOD615X04pCazVE3P'
def get_all_tweets(username,count):
    auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    api=tweepy.API(auth)
    tweets=[]
    new_tweets=api.user_timeline(screen_name=username,count=200)
    tweets.extend(new_tweets)
    leastrecent=tweets[-1].id -1
    while(len(new_tweets)>0):
        new_tweets=api.user_timeline(screen_name=username,count=200,max_id=leastrecent)
        tweets.extend(new_tweets)
        leastrecent=tweets[-1].id-1
        totaltweets=len(tweets)
        if totaltweets>count:
            break
    return [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.retweet_count] for tweet in tweets]
def convert_totxt(tweets):
    with open('newtweet.txt','w') as f:
        f.write('tweets\n')
        for i in tweets:
            
            f.write(str(i[2],'utf-8'))
            f.write('\n')
        f.close()
    with open('newtweetslabels.txt','w') as f:
        f.write('retweets\n')
        for i in tweets:
            
            f.write(str(i[3]))
            f.write('\n')
        f.close()
        
            
if __name__ =='__main__':
    t=get_all_tweets("realDonaldTrump",1500)
    convert_totxt(t)

        
            