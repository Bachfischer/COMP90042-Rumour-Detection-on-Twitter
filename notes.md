## Off-the-shelf BERT with tweet-text only


BERT Base (num_epochs = 5, batch_size = 4) (without proper seperation)
v6


BERT Base (num_epochs = 5, batch_size = 4) (with proper seperation, input_size = 512, perform_stemming = True)
v7


BERT Base (batch_size = 4, perform_stemming=True)
v8


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

BERT Talking Heads base w/ Tensorflow  (num_epochs = 3, batch_size = 4, with sep_token=" ", url + mentions stripped) 
v32

BERT Talking Heads base w/ Tensorflow and COMBINED dataset (num_epochs = 5, batch_size = 4, with sep_token=" ", url + mentions stripped) 
v33

Multimodal BERT (num_epochs = 3, with sep_token=" ", url + mentions stripped) 
v34 (not submitted)

BERTweet (num_epochs = 1) and COMBINED dataset (batch_size = 8, with sep_token=" ", url + mentions stripped) 
v34

BERTweet (num_epochs = 6) and COMBINED dataset (batch_size = 8, with sep_token=" ", url + mentions stripped) 
loaded bertweet v18 
v35

BERTweet (num_epochs = 7) and COMBINED dataset  (batch_size = 8)
v36 (good init..)

Best system by Liu and Wu (2018) "Early detection of fake news on social media through propagation path classification with recurrent and convolutional networks."

-> Further improvements explained in FNED paper
-> Code: https://github.com/yumere/early-fakenews-detection


Papers: https://github.com/JihoChoi/rumor-fake-news-papers