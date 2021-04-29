## Off-the-shelf BERT with tweet-text only


BERT Base (num_epochs = 5, batch_size = 4) (without proper seperation)
v6


BERT Base (num_epochs = 5, batch_size = 4) (with proper seperation, input_size = 512, perform_stemming = True)
v7

BERT Base (num_epochs = 5, batch_size = 4) (with proper seperation, input_size = 512, perform_stemming=False)
v9


BERT Large (num_epochs = 5, batch_size = 2) (with proper seperation, input_size = 512, perform_stemming=False)
v10

BERT Large (num_epochs = 7, batch_size = 2) (with proper seperation, input_size = 512, perform_stemming=False)
v11

BERT Small w/ Tensorflow perform_stemming=False, batch_size = 32)
v12

BERT Small w/ Tensorflow no preprocessing at all!! batch_size = 32
v13

(Kind of similar results as with v12 expected)


BERT Talking Heads base w/ Tensorflow (num_epochs = 5) (perform_stemming=False, batch_size = 8)
v14


BERT Talking Heads base w/ Tensorflow  and COMBINED dataset (num_epochs = 5) (perform_stemming=False, batch_size = 8)
v15


BERT Talking Heads base w/ Tensorflow  and COMBINED dataset (num_epochs = 7)  (perform_stemming=False, batch_size = 4)
v16

BERTweet (num_epochs = 5)  (batch_size = 8)
v17

BERTweet (num_epochs = 5) and COMBINED dataset  (batch_size = 8)
v18

BERTweet (num_epochs = 7) and COMBINED dataset  (batch_size = 8)
v19

BERTweet (num_epochs = 10) and COMBINED dataset  (batch_size = 8)
v20
(using v19 as pretrained model)

BERTweet (num_epochs = 5)  (batch_size = 8, with proper sep_token)
v21

BERTweet (num_epochs = 10)  and COMBINED dataset (batch_size = 8, with proper sep_token)
v22

BERTweet (num_epochs = 20)  and COMBINED dataset (batch_size = 8, with proper sep_token)
v23

BERTweet (num_epochs = 5)  and COMBINED dataset (batch_size = 8, with sep_token=" ")
v24

BERTweet (num_epochs = 7)  and COMBINED dataset (batch_size = 8, with sep_token=" ")
v25

BERTweet (num_epochs = 10)  and COMBINED dataset (batch_size = 8, with sep_token=" ")
v26

BERTweet (num_epochs = 15)  and COMBINED dataset (batch_size = 8, with sep_token=" ")
v27

BERTweet (num_epochs = 5)  and COMBINED dataset (batch_size = 8, with sep_token=" ", url + mentions stripped) 
v28

BERTweet (num_epochs = 5)  (batch_size = 8, with sep_token=" ", url + mentions stripped) 
v29

BERTweet (num_epochs = 5) and COMBINED dataset (batch_size = 8, with sep_token=" ", url + mentions stripped) 
v30

BERTweet (num_epochs = 8) and COMBINED dataset (batch_size = 8, with sep_token=" ", url + mentions stripped) 
v31

## Multi-modal BERT with custom features:
- Calculate user features 
- Calculate tweet features
- Use BERT model to extract tweet embeddings for each tweet text
- Train Model (BERT + MLP)

Experiments: 

BERT Base (batch_size = 4, perform_stemming=True)
v8




Interesting competition: 
Kaggle: https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/code?competitionId=12500&searchQuery=fastai

Notebook: https://www.kaggle.com/alber8295/nb-svm-linear-baseline



Best system by Liu and Wu (2018) "Early detection of fake news on social media through propagation path classification with recurrent and convolutional networks."

-> Further improvements explained in FNED paper
-> Code: https://github.com/yumere/early-fakenews-detection


Papers: https://github.com/JihoChoi/rumor-fake-news-papers

* Conversation trees: 
Github: https://github.com/jerrygaoLondon/RPDNN
Github: https://github.com/serenaklm/rumor_detection

* BERT (from Kaggle challenge)
Kaggle competition: https://www.kaggle.com/c/nlp-getting-started
Kaggle notebook: https://www.kaggle.com/dhruv1234/huggingface-tfbertmodel


* BBERT (from SemEval 2019)
Github: https://github.com/MFajcik/RumourEval2019/tree/master/data_analysis


Other interesting models:

* RoBERTa

* BERTweet:
Kaggle notebook: https://www.kaggle.com/davelo12/bertweet
Kaggle notebook: https://www.kaggle.com/boiledfishpot/twitter-classify-by-bertweet