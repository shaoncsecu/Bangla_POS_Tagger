import os
import HMM

if __name__ == "__main__":

    # This will call the HMM POS tagger. All the paths are specified in Config.py file
    HMM.start()

    # calling the evaluation script provided by our tutor (can be done separately)
    # If you don't have any gold data for the test set, comment this line
    os.system("python Eval.py bn_nltr/data_clean/gold.txt output/test_out.txt")
