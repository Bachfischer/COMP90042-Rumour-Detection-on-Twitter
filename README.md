
# OMP90042-Rumour-Detection-on-Twitter

## Project structure

* `data/` -- Dataset with Twitter data and submissions to competition
* `doc/` -- Documentation and project report
* `src/` -- Source code for processing of tweet data


## Commands

* Calculate evaluation score for predictions:
`python eval.py --predictions dev.baseline.json --groundtruth dev.label.json`
* (DEV) Connect to Tensorboard: `gcloud compute ssh twitter-rumour-detection -- -NfL 6006:localhost:6006`