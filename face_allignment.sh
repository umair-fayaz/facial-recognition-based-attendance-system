#!/bin/sh
# align testing images
python ~/facial-recognition-based-attendance-system/src/align/align_dataset_mtcnn.py \
~/facial-recognition-based-attendance-system/data/images/test_raw \
~/facial-recognition-based-attendance-system/data/images/test_aligned \
--image_size 160
