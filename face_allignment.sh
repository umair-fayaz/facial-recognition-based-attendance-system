#!/bin/sh
# align testing images
python ~/facial_recognition_based_attendance_system/src/align/align_dataset_mtcnn.py \
~/facial_recognition_based_attendance_system/data/images/test_raw \
~/facial_recognition_based_attendance_system/data/images/test_aligned \
--image_size 160
