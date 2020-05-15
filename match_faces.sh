#!/bin/sh
# Test face matches using pickle file to classify matching images
python ~/facial_recognition_based_attendance_system/src/classifier.py CLASSIFY \
~/facial_recognition_based_attendance_system/data/images/test_aligned/ \
~/facial_recognition_based_attendance_system/models/20180402-114759.pb \
~/facial_recognition_based_attendance_system/models/my_classifier.pkl
