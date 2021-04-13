import argparse
import sys
import json
from sklearn.metrics import precision_recall_fscore_support

#parameters
debug = False

###########
#functions#
###########

def convert_label(label):
    if label == "rumour":
        return 1
    elif label == "non-rumour":
        return 0
    else:
        raise Exception("label classes must be 'rumour' or 'non-rumour'")

######
#main#
######

def main(args):

    groundtruth = json.load(open(args.groundtruth))
    predictions = json.load(open(args.predictions))

    y_true, y_pred = [], []

    try:
        for k, v in groundtruth.items():
            if k in predictions:
                y_pred.append(convert_label(predictions[k]))
            #if ID isn't in predictions, assume incorrect predictions
            else:
                y_pred.append(int(not(bool(convert_label(v)))))
            y_true.append(convert_label(v))

        p, r, f, _ = precision_recall_fscore_support(y_true, y_pred, pos_label=1, average="binary")
    except Exception as error:
        print("Error:", error)
        raise SystemExit


    print("Performance on the rumour class:")
    print("Precision =", p)
    print("Recall    =", r)
    print("F1        =", f)
        

if __name__ == "__main__":

    #parser arguments
    desc = "Computes precision, recall and F-score of the rumour class"
    parser = argparse.ArgumentParser(description=desc)

    #arguments
    parser.add_argument("--predictions", required=True, help="json file containing system predictions")
    parser.add_argument("--groundtruth", required=True, help="json file containing ground truth labels")
    args = parser.parse_args()

    main(args)
