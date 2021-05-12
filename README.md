# COMP90042-Rumour-Detection-on-Twitter

This repository contains the source code for the *Rumour Detection and Analysis on Twitter* Project that was part of the COMP90042 Natural Language Processing course at the University of Melbourne.

## Project structure

* `data/` -- Raw datasets published by COMP90042 competition organizers
* `doc/` -- Documentation and project report (LaTeX source)
* `src/` -- Source code for task 01 (rumour identification) and task 02 (rumour analysis)
    * `01_rumour_detection_bertweet.ipynb` -- Notebook using pre-trained [BERTweet model](https://github.com/VinAIResearch/BERTweet) (task 01)
    * `01_rumour_detection_multimodal_bert.ipynb` -- Notebook with implementation of [Multimodal Toolkit](https://github.com/georgian-io/Multimodal-Toolkit) architecture (task 01)
    * `01_rumour_detection_tf_with_huggingface_model_hub.ipynb` -- Notebook using pre-trained BERT models from [Hugging Face Model Hub](https://huggingface.co/models) (task 01)
    * `01_rumour_detection_tf_with_tf_hub.ipynb` -- Notebook using pre-trained BERT models from [Tensorflow Hub](https://tfhub.dev) (task 01)
    * `02_rumour_analysis.ipynb` -- Notebook with analyses to understand the nature COVID-19 rumours and how they differ to their non-rumour counterpart (task 02)
    * `dataloader.py` -- Source code shared by multiple notebooks for loading and processing Twitter data
* `submissions/` -- Submissions to the COMP90042 CodaLab competition ([Link to competition](https://competitions.codalab.org/competitions/30503))


For further information, please refer to the project report attached to this submission.