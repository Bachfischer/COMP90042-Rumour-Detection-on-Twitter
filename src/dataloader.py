import json
import re
import sys
import pandas as pd
import numpy as np
import spacy

nlp = spacy.load("en_core_web_sm")


def convert_label(label):
    if label == "rumour":
        return 1
    elif label == "non-rumour":
        return 0
    else:
        raise Exception("label classes must be 'rumour' or 'non-rumour'")
        
        
def convert_prediction(pred):
    if pred == 1:
        return "rumour"
    elif pred == 0:
        return "non-rumour"
    else:
        raise Exception("prediction classes must be '0' or '1'")
        
        
def extract_features(tweet):
    tweet_features = {}
    
    ### Tweet features
    tweet_features['text'] = tweet['text']
    
    # Number of retweets
    tweet_features['retweet_count'] = tweet['retweet_count']
    # Number of favorites
    tweet_features['favorite_count'] = tweet['favorite_count']
    
    #Whether tweet has a question mark
    tweet_features['question_mark'] = '?' in tweet['text']
    
    # Whether tweet contains URLs
    if 'urls' in tweet['entities']:
        number_of_urls = len(tweet['entities']['urls'])
    else: 
        number_of_urls = 0
        
    tweet_features['contains_url'] = True if number_of_urls > 0 else False
    
    # Number of URLs embedded in tweet
    tweet_features['number_urls'] =  number_of_urls
    
    # Whether tweet has native media
    if 'media' in tweet['entities']:
        number_of_media = len(tweet['entities']['media'])
    else: 
        number_of_media = 0
        
    tweet_features['contains_media'] = True if number_of_media > 0 else False
    
    
    ### User features
    user_features = {}
    
    # Number of posts user has posted
    user_features['statuses_count'] = tweet['user']['statuses_count']
    
    # Number of public lists user belongs to
    user_features['listed_count'] = tweet['user']['listed_count']


    # Number of followers
    user_features['followers_count'] = tweet['user']['followers_count']

    # Number of followings
    user_features['friends_count'] = tweet['user']['friends_count']

    # Whether user has a background profile image
    if 'profile_background_image_url' in tweet['user']:
        profile_background_image_url = True
    else:
        profile_background_image_url = False
    
    user_features['contains_profile_background_image'] = profile_background_image_url
    
    # User reputation (i.e., followers/(followings+1))
    user_features['reputation_score_1'] = user_features['followers_count'] / ( user_features['friends_count'] +1)
    
    # User reputation (i.e., followers/(followings+followers+1))
    user_features['reputation_score_2'] = user_features['followers_count'] /(user_features['followers_count'] +
                                                                              user_features['friends_count'] +1)

    # Number of tweets user has liked so far (aka ”user favorites”)
    user_features['favourites_count'] = tweet['user']['favourites_count']

    # Account age in days
    # TODO
    
    # Following rate (i.e., followings / (account age+1))
    # TODO
    
    # Favorite rate (i.e., user favorites / (account age+1))
    # TODO
    
    # User engagement (i.e., # posts / (account age+1))
    # TODO
    
    # Response time decay (time difference between context and source tweet in mins)
    # TODO
    
    # Whether user is verified
    user_features['verified'] = tweet['user']['verified']

    # Whether geolocation is enabled
    user_features['geo_enabled'] = tweet['user']['geo_enabled']

    # Number of words in user description
    if 'description' in tweet['user'] and tweet['user']['description'] != None:
        length_description = len(tweet['user']['description'])
    else:
        length_description = 0
        
    # Whether user has a description
    user_features['has_description'] = True if length_description > 0 else False
        
    # Length of user description
    user_features['length_description'] = length_description

    
    # Merge features
    tweet_features.update(user_features)
    return tweet_features

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

def preprocessing(text, perform_stemming):
    text = text.replace('#','')
    text = decontracted(text)
    text = re.sub('\S*@\S*\s?','',text)
    
    if perform_stemming == True:
        text = re.sub('http[s]?:(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',text)
        text = re.sub('[^A-z]', ' ',text.lower())
    else:
        text = re.sub('http[s]?:(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),])+','',text)
        text = re.sub('[^A-z]', ' ',text.lower())
    
    if perform_stemming == True:

        token = []
        result =''

        text = nlp(text)
        for t in text:
            if not t.is_stop and len(t)>2:  
                token.append(t.lemma_)
        result = ' '.join([i for i in token])
    else:
        result = text
        
    return result.strip()

def load_data(data_file, label_file, perform_stemming):
    
    if label_file != None:
        y_true = json.load(open(label_file))
    
    with open(data_file, 'r') as data_train:
        raw_list = list(data_train)

    data_list = []


    for event in raw_list:
        tweets_in_event = json.loads(event)
        
        ## Task 1
        tweet = {}
        tweet['id'] = tweets_in_event[0]['id']
        tweet.update(extract_features(tweets_in_event[0]))
        
        tweet['text'] = preprocessing(tweets_in_event[0]['text'], perform_stemming)
        # append text from follow-up tweets in tweet chain
        follow_up_tweets = ""
        for i in range(1, len(tweets_in_event)):
            #follow_up_tweets = follow_up_tweets + tweets_in_event[i]['text'] + " [SEP] "
            follow_up_tweets = follow_up_tweets + preprocessing(tweets_in_event[i]['text'], perform_stemming) + " "
        
        # Concatenate text from all tweets in field 'text'
        #tweet['text'] = tweet['text'] + " [SEP] " + follow_up_tweets
        tweet['text'] += " " + follow_up_tweets
        tweet['text'] = tweet['text'].strip()

        ## Task 2
        tweet['source_tweet'] = preprocessing(tweets_in_event[0]['text'], perform_stemming)  

        tweet['replies'] = []
        for i in range(1, len(tweets_in_event)):
            reply = preprocessing(tweets_in_event[i]['text'], perform_stemming)
            if len(reply) > 0:
                tweet['replies'].append(reply)

        tweet['hashtags'] = []
        for i in range(0, len(tweets_in_event)):
            if len(tweets_in_event[i]['entities']['hashtags']) > 0:
                for hashtag in tweets_in_event[i]['entities']['hashtags']:
                    hashtag_lower = hashtag['text'].lower()
                    tweet['hashtags'].append(hashtag_lower)


        if label_file != None:
            tweet['label'] = convert_label(y_true[str(tweet['id'])])
        
        data_list.append(tweet)

    df = pd.DataFrame(data_list)

    return df