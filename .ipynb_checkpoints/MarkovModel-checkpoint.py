class Model(object):
    def __init__(self,corpus):
        self.corpus=corpus
    def model(self):
        markov_dict = {'<start>':[]}
        starting_words = []
        for tweet in self.corpus.tweets:
            tok_tweet = tweet.split()
            word_count = len(tok_tweet)
            for index, word in enumerate(tok_tweet):
                if word not in markov_dict.keys():
                    markov_dict[word] = []

                if index == word_count - 1:
                    markov_dict[word].append("<end>")
                
                else:
                    if index == 0:
                        starting_words.append(word)
                    markov_dict[word].append(tok_tweet[index+1])
        return markov_dict, starting_words
        
    def write_tweet(self,starting_word, chain):
        
        tweet = starting_word
        current_word = starting_word

        while len(tweet) <= 140:        
            next_word = np.random.choice(chain[current_word])
            if next_word == '<end>':
                return(tweet)

            new_tweet = tweet + ' ' + next_word
            if  len(new_tweet) > 140:
                return(tweet)
            else:
                tweet = new_tweet
                current_word = next_word
    
if __name__=='__main__':
    import pandas as pd
    import numpy as np
    tweets=pd.read_csv('/home/aidris/Pictures/twitterSNA/cleanedtweets.csv')
    markov=Model(tweets)
    i=1
    markov_dict, starting_words=markov.model()
    pred_tweets=[]
    while True:
        starting_word = np.random.choice(starting_words)
        pred_tweet=markov.write_tweet(starting_word, markov_dict)
        pred_tweets.append(pred_tweet)
        if(i<20):
            print(str(pred_tweets)+"\n")
        i+=1
    pred_tweets=pd.Series(pred_tweets)
    df=pd.DataFrame()
    df['predicted_tweets']=pred_tweets
    print(df)
    #df['predicted_tweets'].to_csv('predictedTWEETS.csv')
