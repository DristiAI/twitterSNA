import pandas as pd
import random 
import nltk
df=pd.read_csv('cleanedtweets.csv')
def f(x):
    return x.split()

def makepairs(arr):
    pairs=[]
    for i in range(len(arr)):
        if i<len(arr)-1:
            temp=(arr[i],arr[i+1])
            pairs.append(temp)
    return pairs

def generate(cfd, word = 'the', num = 50):     
     for i in range(num):         
          arr = []           # an array with the words shown by count     
          for j in cfd[word]:             
               for k in range(cfd[word][j]):                 
                    arr.append(j)                  
                    #print(word, end=' ')         
                    word = arr[int((len(arr))*random.random())] 
                    print(word, end=' ') 
pairs=makepairs(df['tweets'])
cfd=nltk.ConditionalFreqDist(pairs)
generate(cfd)
