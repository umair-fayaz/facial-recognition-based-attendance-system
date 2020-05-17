#!/bin/sh
# Test face matches using pickle file to classify matching images
python ~/facial-recognition-based-attendance-system/src/classifier.py CLASSIFY \
~/facial-recognition-based-attendance-system/data/images/test_aligned/ \
~/facial-recognition-based-attendance-system/models/20180402-114759.pb \
~/facial-recognition-based-attendance-system/models/my_classifier.pkl
