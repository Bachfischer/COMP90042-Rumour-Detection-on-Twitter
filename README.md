
# OMP90042-Rumour-Detection-on-Twitter

## Project structure

* `data/` -- Raw datasets published by competition organizers
* `doc/` -- Documentation and project report (LaTeX source)
* `src/` -- Source code for task 01 (rumour identification) and task 02 (rumour analysis)
    * `01_rumour_detection_bertweet.ipynb` -- Notebook using pre-trained [BERTweet model](https://github.com/VinAIResearch/BERTweet)
    * `01_rumour_detection_multimodal_bert.ipynb` -- Notebook with implementation of [Multimodal Toolkit](https://github.com/georgian-io/Multimodal-Toolkit) architecture
    * `01_rumour_detection_tf_with_huggingface_model_hub.ipynb` -- Notebook using pre-trained BERT models from [Hugging Face Model Hub](https://huggingface.co/models)
    * `01_rumour_detection_tf_with_tf_hub.ipynb` -- Notebook using pre-trained BERT models from [Tensorflow Hub](https://tfhub.dev)
    * `02_rumour_analysis.ipynb` -- Notebook with analyses to understand the nature COVID-19 rumours and how they differ to their non-rumour counterpart
    * `dataloader.py` -- Source code shared across the notebooks for loading and processing Twitter data
* `submissions/` -- Submissions to the COMP90042 CodaLab competition ([Link to competition](https://competitions.codalab.org/competitions/30503))